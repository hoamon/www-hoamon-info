#!/usr/bin/python
# -*- coding: utf8 -*-
import os
from optparse import OptionParser, OptionGroup
from mercurial import ui, hg, error, commands



class NonCommitError(Exception):
    """ repository has some change, but no commit
    """
    pass



class AdvanceHG(object):
    """ """


    def __init__(self, *args, **options):
        u""" check user input

            depends_modules.conf example:

            [depends]
            #若有其他想要加入的模組，可自行加在 depends_modules.conf 中
            # :xxxyyyzzz 代表特定版本的 changeset 碼，若無設定代表 tip
            # 有設定 :xxxyyyzzz 後，則該模組只會 update 至該版本。但 pull 還是會抓到 tip 版
            apps/common:8f31f65649e4 = https://hg.nchu-cm.com/repo/modules/common
            apps/dailyreport:420226396cd6 = https://hg.nchu-cm.com/repo/modules/dailyreport
            apps/engphoto:feb832120670 = https://hg.nchu-cm.com/repo/modules/engphoto
            apps/general:8843030f10bb = https://hg.nchu-cm.com/repo/modules/general
            apps/webcpm = https://hg.nchu-cm.com/repo/modules/webcpm
        """

        self.op = op = OptionParser(usage = "usage: ./%prog [OPTIONS]... [REPOS]...",
                                    version = "%prog, $Revision: ??? $")

        opg = OptionGroup(op, u"Pull All HG Project")

        opg.add_option("-r", "--pullall", action="callback", callback=self.pullAll,
            type="string", help=u"將指定的主資料夾內，其相依的 hg 專案作 hg pull ")

        opg.add_option("-j", "--jump", action="store_true", dest="jump_non_commit",
            help=u"跳過需要 commit 的 hg 專案")

        opg.add_option("-p", "--proxy", action="store", dest="proxy",
            type="string", help=u"手動指定 http_proxy 位置格式如：http://172.22.100.100:8080/。須放置於 --pullall 之後。")

        opg.add_option("-d", "--depends", action="store", dest="depends",
            type="string", help=u"手動指定同步更新的模組資料夾，可多值設定，但本參數須放置於 --pullall 之後。如無設定，則自動讀取主資料夾中的 depends_modules.conf 來處理")
        self.depends_modules = 'depends_modules.conf'

        op.add_option_group(opg)

        if not options:
            (_options, _args) = op.parse_args()


    def checkNoDiff(self, repo):
        if repo.status()[0]:
            raise NonCommitError(u'該 %s 專案尚有修改未 commit ，請先 commit 後再作 pull'%repo.root)


    def rConfig(self, key_name, directory, hgrc_filename=''):
        if hgrc_filename:
            if not os.path.isfile(os.path.join(directory, hgrc_filename)):
                return []
        else:
            hgrc_filename = os.path.join('.hg', 'hgrc')


        ui0 = self.ui0
        ui00 = ui0.copy()
        ui00.readconfig(os.path.join(directory, hgrc_filename))
        paths = [config[-2:] for config in ui00.walkconfig()
            if config[0] == key_name and config[1] != 'default-push']
        if not paths:
            raise ValueError(u'該 %s 專案的 hgrc 無 default-pull or default 設定'%directory)
        return paths


    def rDepends(self, directory, hgrc_filename=''):
        return self.rConfig('depends', directory, hgrc_filename)


    def rPaths(self, directory, hgrc_filename=''):
        return self.rConfig('paths', directory, hgrc_filename)


    def pull(self, directory, version=''):
        u""" 所 pull 的路徑必須寫在 .hg/hgrc 中，且帳號/密碼須事先定義
        """

        ui0 = self.ui0
        ui0.write(u'== 目前正在處理 %s 資料夾 ==\n' % directory)
        try:
            repo = hg.repository(ui0, directory)
        except error.RepoError:
            raise ValueError(u'%s 不是 hg 專案'%directory)

        try:
            self.checkNoDiff(repo)
        except NonCommitError, e:
            if self.jump_non_commit:
                ui0.write(u'\t# Need Commit, jump %s 專案\n' % directory)
                return
            else:
                raise NonCommitError(e)

        paths = self.rPaths(directory)

        remote = hg.repository(ui0, paths[-1][-1])
        repo.pull(remote, force=True)
        if not version:
            version = 'tip'
        hg.update(repo, version)
        ui0.write(u'\t 更新至 %s 版\n' % version)


    def pullAll(self, *args, **kw):
        print(u'\tpullAll: begin')
        self.ui0 = ui0 = ui.ui()
        self.pullall_directory = pullall_directory = args[2]
        try:
            self.depends = depends = args[3].rargs
        except IndexError:
            self.depends = depends = []

        if '-j' in depends:
            self.jump_non_commit = True
            depends.remove('-j')
        elif '--jump' in depends:
            self.jump_non_commit = True
            depends.remove('--jump')
        else:
            self.jump_non_commit = False
            if '-d' in depends:
                depends.remove('-d')
            elif '--depends' in depends:
                depends.remove('--depends')

        if '-p' in depends:
            idx = depends.index('-p')
            proxy = depends[idx+1]
            depends.remove('-p')
            depends.remove(proxy)
        elif '--proxy' in depends:
            idx = depends.index('--proxy')
            proxy = depends[idx+1]
            depends.remove('--proxy')
            depends.remove(proxy)
        else:
            proxy = ''

        ui0.setconfig('http_proxy', 'host', proxy)
        repo = self.pullall_directory.split(':')[0]
        self.pull(repo)

        if not depends:
            paths = self.rDepends(pullall_directory, hgrc_filename=self.depends_modules)
            for path in paths:
                try:
                    repo, version = path[0].split(':')
                except ValueError:
                    repo = path[0].split(':')[0]
                    version = None
                if os.path.isdir(os.path.join(pullall_directory, repo)):
                    self.pull(os.path.join(pullall_directory, repo), version)
                else:
                    remote_source = path[1]
                    #TODO should change to mercurial api
                    os.popen('hg clone %s %s' % (remote_source, os.path.join(pullall_directory, repo)))
                    self.pull(os.path.join(pullall_directory, repo), version)
        else:
            for depend in depends:
                self.pull(depend)

        print(u'\tpullAll: done')


if __name__ == '__main__':
    AdvanceHG()
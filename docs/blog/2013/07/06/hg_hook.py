#!/usr/bin/python
import os, re


def merge_sigcheck(*args, **kw):
    """ put two lines below here into .hgrc:
        [hooks]
        pre-merge = python:/path/hoamon_hg_hook:merge_sigcheck
    """
    type_version = kw['opts']['rev']
    merge_version = os.popen('hg log -r %s^ --template "{node|short}"'%type_version).read()
    res = os.popen('hg sigcheck %s'%merge_version).read()
    if ' signed ' in res:
        return False
    elif ' -f' in kw['args']:
        return False
    else:
        print('changeset:"%s" has no GPG signature!\n'%type_version)
        return True


def autosign(*args, **kw):
    """ put two lines below here into .hgrc:
        [hooks]
        pre-push = python:/path/hoamon_hg_hook:autosign

        execute flow:

            1. Grep username and public key id from hgrc.
            2. Do the head-1 changeset of this batch wanted to push has a signature?
                1. Yes => No need to sign GPG signature.
                2. No =>
                    1. The author of head changeset is not me => show a message: "The newest changeset is not yours".
                    2. The author of head changeset is me or "push -f" in shell command => sign a signature.
    """
    print('HG Push Start...\n')

    author_name = kw['ui'].username()
    public_key_id = kw['ui'].config('gpg', 'key')
    public_key_url = kw['ui'].config('gpg', 'key_url')
    key_info = os.popen('gpg --list-public-keys %s'%public_key_id).read()
    public_key_uid = re.search(r'uid\s+([^\n]+)', key_info).groups()[0]
    print('Author Name: %s\n'%author_name)
    print('Public Key UID: %s\n'%public_key_uid)

    check_version = os.popen('hg log -r tip^ --template "{node|short}"').read()
    res = os.popen('hg sigcheck %s'%check_version).read()

    if public_key_uid in res:
        print('No need to sign GPG signature!\n')
        return False
    else:
        print('Head Changeset:\n')
        res0 = os.popen('hg tip -v').read()
        for line in res0.split('\n'): print('\t%s'%line)

        if not re.search(r'\b'+author_name+r'\b', res0) and "push -f" not in kw['args']:
            print('The newest changeset is not yours\n')
            return True
        else:
            version = re.search(r'changeset:\s+[0-9]+:([^\s]+)\s', res0).groups()[0]
            r = os.popen('hg sign %(version)s -m "Added signature(with id:%(key_id)s %(key_url)s) for changeset %(version)s"'%
                        {'version': version,
                        'key_id': public_key_id,
                        'key_url': public_key_url,
                        })
            print('Done for %s\n'%r.read())
            return False


if __name__ == '__main__':
    print('return %s' % autosign())

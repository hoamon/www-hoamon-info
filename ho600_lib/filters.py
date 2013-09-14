from django.conf import settings
from django.utils.encoding import smart_str
from mediagenerator.generators.bundles.base import Filter

class Glue(Filter):
    def __init__(self, **kwargs):
        super(Glue, self).__init__(**kwargs)


    def get_output(self, variation):
        # We import this here, so App Engine Helper users don't get import
        # errors.
        #from subprocess import Popen, PIPE
        for input in self.get_input(variation):
            yield input + '\n'
            #yield open(input).read() + '\n'
#             try:
#                 compressor = settings.YUICOMPRESSOR_PATH
#                 cmd = Popen(['java', '-jar', compressor,
#                              '--charset', 'utf-8', '--type', self.filetype],
#                             stdin=PIPE, stdout=PIPE, stderr=PIPE,
#                             universal_newlines=True)
#                 output, error = cmd.communicate(smart_str(input))
#                 assert cmd.wait() == 0, 'Command returned bad result:\n%s' % error
#                 yield output.decode('utf-8')
#             except Exception, e:
#                 raise ValueError("Failed to execute Java VM or yuicompressor. "
#                     "Please make sure that you have installed Java "
#                     "and that it's in your PATH and that you've configured "
#                     "YUICOMPRESSOR_PATH in your settings correctly.\n"
#                     "Error was: %s" % e)

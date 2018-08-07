import sys


class botcommands:
    def cmd_test():
        return ('cmd_test 실행됨')

    def cmd_timer():
        return ('cmd_timer 실행됨')

    def cmd_test():
        return ('cmd_test 실행됨')

    commandlist = {'!커맨드': 'cmd_test',
                   '!타이머': 'cmd_timer',
                   '!테스트': 'cmd_test'}

    def runcommand(cmdname):
        return local()[commandlist[cmdname]]()


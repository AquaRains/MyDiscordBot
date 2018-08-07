import sys
import asyncio

commandlist = {'!커맨드': 'cmd_cmd',
               '!타이머': 'cmd_timer',
               '!테스트': 'cmd_test'}


def cmd_test():
    return ("""!테스트 명령어가 실행되었습니다.
현재 멀쩡하게 돌아가는거 같네요
귀찮으니까 다른거 테스트 해보셈""")


def cmd_timer():
    return ('타이머 로직이 들어갈 자리')


def cmd_cmd():
    return ('cmd_cmd 실행됨')


async def runcommand(cmdname):
    try:
        return globals()[commandlist[cmdname]]()
    except Exception as ex:
        print(ex)
        return ex
        pass


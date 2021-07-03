# https://programmers.co.kr/learn/courses/30/lessons/17683

#일단 틀어준 음악을 이름을 구분해서 연주한 시간에 맟춰서 늘어놓는다. 
#윈도우슬라이딩을 이용해서 기억한 "음"길이 만큼 가져와서 대조한다. 
#단 여러개의 조건이 생길때면 -> 라디오재생길이가 가장 긴 음악제목(1) -> 재생시간 동일시 '먼저 입력된' 음악제목 반환 1개만 반환!
#83.3 -> 86.7 (16,20(런타임),27,30)


'''
def solution(m, musicinfos):
    answer = ''

    answerList = []
    playindex = 0

    for playMusic in musicinfos:
        playindex+=1
        startTime, endTime, songName, songCode = playMusic.split(',')       #입력받은 음악정보를 분리
        print(startTime, endTime, songName, songCode)

        playTime = ((int(endTime[:2]) * 60) + int(endTime[3:])) - ((int(startTime[:2]) * 60) + int(startTime[3:]))  #방송시간을 분단위로 계산
        platTimeFix = playTime
        print('방송시간',playTime,'분')

        if m == songCode:
            answerList.append((platTimeFix, playindex, songName))

        playlog = ''
        p=0
        while playTime:
            if p < (len(songCode) - 1) and songCode[p+1] == '#':
                playlog += songCode[p] + songCode[p+1]
                playTime -= 1
                p+=2

            else:
                playlog += songCode[p]
                playTime -= 1
                p += 1

            if p>=len(songCode):
                p=0

        print('해당시간에 송출된 코드',playlog)

        if len(m) < len(playlog)-1 and playlog[len(m)] == '#':
            compareCode = playlog[:len(m)+1]
            pp = len(m)+1
        else:
            compareCode = playlog[:len(m)]
            pp = len(m)

        print('초기 검사코드', compareCode)

        while pp < len(playlog)+1:                        #조건이 총4가지있음. 비교코드에 추가할 코드가 #일때와 아닐때(2가지) * 비교코드에서 빼낼 코드가 #일때와 아닐때(2가지)
            print('55번줄',m, '과',compareCode,'를 비교',pp)
            
            if compareCode == m :   #비교코드가 기억하고있는 코드와 동일할때는 중지
                print('찾았다')
                answerList.append((platTimeFix, playindex, songName))
                break
            
            if pp >= len(playlog):  #다음에 문자를 가져올 포인터가 playlog범위를 벗어날경우
                break

            if pp < len(playlog)-1 and playlog[pp+1] == '#' and len(compareCode)>1 and compareCode[1] == "#": # input# output#
                print('1.in# out#')
                compareCode = compareCode[2:] + playlog[pp] + playlog[pp+1]
                pp+=2
            
            elif pp < len(playlog) and playlog[pp+1] == '#' and len(compareCode)>1 and compareCode[1] == "#": # input# output#
                print('1.in# out#')
                compareCode = compareCode[2:] + playlog[pp] + playlog[pp+1]
                pp+=2
                
            elif pp < len(playlog)-1 and playlog[pp+1] == '#' and len(compareCode)>1 and compareCode[1] != "#" : # input# output not #   
                print('2.in# out not#')
                compareCode = compareCode[1:] + playlog[pp] + playlog[pp+1]
                pp+=2
            
            elif pp < len(playlog)-1 and playlog[pp+1] != '#' and len(compareCode)>1 and compareCode[1] == "#": # input not# output#
                print('3.in not# out#')
                compareCode = compareCode[2:] + playlog[pp]
                pp+=1

            else:       #input not # output not #
                print('4.in not# out not#')
                compareCode = compareCode[1:] + playlog[pp]
                pp+=1

            print('85번줄','한칸 슬라이딩한 결과',compareCode,pp)
            print('-'*50)
        
        print('='*50)

        #기억하는 길이가 곡보다 더 길어서 반복된것을 분할해서 확인해야할때
        

        
    print(answerList)

    if not answerList:                                      #조건 전부 불일치시 None 반환
        answer = '(None)'
    else:
        answerList.sort(key = lambda x: (-x[0], x[1]))      #부합하는 요소 존재시, 재생시간이 긴것(-x[0])을 우선 -> 재생시간 동일시 먼저 재생된것(x[1])을 우선으로 정렬하여 맨앞값 하나만 반환
        answer = answerList[0][2]

    return answer
    '''


'''
def solution(m, musicinfos):
    answer = ''

    answerList = []
    playindex = 0

    for playMusic in musicinfos:
        playindex+=1
        startTime, endTime, songName, songCode = playMusic.split(',')       #입력받은 음악정보를 분리

        playTime = ((int(endTime[:2]) * 60) + int(endTime[3:])) - ((int(startTime[:2]) * 60) + int(startTime[3:]))  #방송시간을 분단위로 계산
        platTimeFix = playTime

        if m == songCode:
            answerList.append((platTimeFix, playindex, songName))

        playlog = ''
        p=0
        while playTime:
            if p < (len(songCode) - 1) and songCode[p+1] == '#':
                playlog += songCode[p] + songCode[p+1]
                playTime -= 1
                p+=2

            else:
                playlog += songCode[p]
                playTime -= 1
                p += 1

            if p>=len(songCode):
                p=0

        if len(m) < len(playlog)-1 and playlog[len(m)] == '#':
            compareCode = playlog[:len(m)+1]
            pp = len(m)+1
        else:
            compareCode = playlog[:len(m)]
            pp = len(m)

        while pp < len(playlog)+1: 
            
            if compareCode == m :   #비교코드가 기억하고있는 코드와 동일할때는 중지
                answerList.append((platTimeFix, playindex, songName))
                break
            
            if pp >= len(playlog):  #다음에 문자를 가져올 포인터가 playlog범위를 벗어날경우
                break
            

            if pp < len(playlog) -1:        #가져올코드가 맨뒤에서 2번째까지검사 -> 여기서 A#가 추가되면 바로 다음검사가 마지막검사가 되며, A가 추가되면 다음검사에서 else추가후 한번더 검사를 수행
                compareCode += playlog[pp] + playlog[pp+1]
                if compareCode[-1] == '#':  #새로 가져오는 코드가 A인지 A#인지 구분
                    pp+=2
                else:
                    compareCode = compareCode[:-1]
                    pp+=1

                if compareCode[1] == '#':   #버릴 맨처음코드가 A인지 A#인지 구분(먼저 가져왔으므로 최소한의 길이는 2이다)
                    compareCode = compareCode[2:]
                else:
                    compareCode = compareCode[1:]

            else:                           #여기는 맨마지막에 A가 있을때만 오게된다
                compareCode += playlog[pp]
                pp+=1

                if compareCode[1] == '#':   #버릴 맨처음코드가 A인지 A#인지 구분(먼저 가져왔으므로 최소한의 길이는 2이다)
                    compareCode = compareCode[2:]
                else:
                    compareCode = compareCode[1:]

    if not answerList:                                      #조건 전부 불일치시 None 반환
        answer = '(None)'
    else:
        answerList.sort(key = lambda x: (-x[0], x[1]))      #부합하는 요소 존재시, 재생시간이 긴것(-x[0])을 우선 -> 재생시간 동일시 먼저 재생된것(x[1])을 우선으로 정렬하여 맨앞값 하나만 반환
        answer = answerList[0][2]

    return answer
'''


def solution(m, musicinfos):
    answer = ''

    answerList = []
    playindex = 0

    m += '0'
    memory = []
    m1 = 0
    while m1 < len(m)-1:                    #기억하고있는 코드를 List화하는 과정.
        if m[m1+1] == '#':
            memory.append(m[m1]+m[m1+1])
            m1+=2
        else:
            memory.append(m[m1])
            m1+=1

    memoryLength = len(memory)

    for playMusic in musicinfos:
        playindex+=1
        startTime, endTime, songName, songCode = playMusic.split(',')       #입력받은 음악정보를 분리

        playTime = ((int(endTime[:2]) * 60) + int(endTime[3:])) - ((int(startTime[:2]) * 60) + int(startTime[3:]))  #방송시간을 분단위로 계산
        playTimeFix = playTime

        songCode += '0' #null문자 역할을 수행할 마지막문자 0을 노래맨뒤에 붙임
        songNotes = []
        p1 = 0
        while p1 < len(songCode)-1:                     #원래 음악의 노트 문자열배열을 리스트화
            if songCode[p1+1] == '#':
                songNotes.append(songCode[p1]+songCode[p1+1])
                p1+=2
            else:
                songNotes.append(songCode[p1])
                p1+=1

        songLength = len(songNotes)
        playLog = []
        p2=0
        while playTime: 
            playLog.append(songNotes[p2])
            p2+=1
            playTime-=1

            if p2 == songLength:
                p2=0

        compareNotes = []
        p2=0
        while p2 + memoryLength -1 < playTimeFix:
            compareNotes = playLog[p2:p2+memoryLength]
            p2+=1

            if compareNotes == memory:
                answerList.append((playTimeFix, playindex, songName))
                break

    if not answerList:                                      #조건 전부 불일치시 None 반환
        answer = '(None)'
    else:
        answerList.sort(key = lambda x: (-x[0], x[1]))      #부합하는 요소 존재시, 재생시간이 긴것(-x[0])을 우선 -> 재생시간 동일시 먼저 재생된것(x[1])을 우선으로 정렬하여 맨앞값 하나만 반환
        answer = answerList[0][2]

    return answer


m, musicinfos = "A#BC", ["12:00,12:15,대충이름,CC#A#B"]

print(solution(m, musicinfos))


# C D E F G A B C D E F G A B index는 0~13까지
#  D#EF#G#D#EF#G#D#EF#G#D#EF#
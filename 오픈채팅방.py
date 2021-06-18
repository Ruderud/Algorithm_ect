#https://programmers.co.kr/learn/courses/30/lessons/42888

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]



# def solution(record):
#     answer = []
#     chatroom = []

#     inout_log = []

#     for log in record:
#         data = list(log.split(" "))

#         if len(data) == 3 and data[0] == 'Enter':
#             state, uid, nickname = True, data[1], data[2]
#             if uid in [ user[1] for user in chatroom ]:     #만일 해당 uid의 유저가 채팅방에 온적이있다면 닉네임을 현재 입장닉네임으로 바꾼다
#                 for i in chatroom:
#                     if i[1] == uid:
#                         i[2] = nickname
#             else: 
#                 chatroom.append([state, uid, nickname])     #없다면 신규추가한다.
            
#             inout_log.append((state,uid))                   #그리고 출입로그에 입장기록을 추가한다.

#         elif len(data) == 3 and data[0] == 'Change':        #채팅방 내부에서 닉네임을 바꿀때
#             uid, nickname = data[1], data[2]
#             for i in chatroom:
#                 if i[1] == uid:
#                     i[2] = nickname


#         else:                                               #채팅방에서 나갈때
#             state, uid = False, data[1]
#             for i in chatroom:
#                 if i[1] == uid:
#                     i[0] = False
#             inout_log.append((state,uid))
            
#     for message in inout_log:
#         if message[0]:
#             for i in chatroom:
#                 if i[1] == message[1]:
#                     name = i[2]
#             answer.append(name + "님이 들어왔습니다.")
        
#         else:
#             for i in chatroom:
#                 if i[1] == message[1]:
#                     name = i[2]
#             answer.append(name + "님이 나갔습니다.")

#     return answer

# print(solution(record))



def solution(record):
    answer = []

    userList = { }  # 1234:[true, prodo] 꼴
    inoutLog = []

    for log in record:
        data = log.split()

        if log[0] == 'E':
            userList[data[1]]=[True, data[2]]
            inoutLog.append((True, data[1]))
            
        elif log[0] == 'L':
            userList[data[1]][0] = False
            inoutLog.append((False, data[1]))
        else:       #Change일때
            userList[data[1]][1]=data[2]

    for message in inoutLog:
        if message[0]:
            answer.append(userList[message[1]][1] + "님이 들어왔습니다.")
        else:
            answer.append(userList[message[1]][1] + "님이 나갔습니다.")

    return answer

print(solution(record))

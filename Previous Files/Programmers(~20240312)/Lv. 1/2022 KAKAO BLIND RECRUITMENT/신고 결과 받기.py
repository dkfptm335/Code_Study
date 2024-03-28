def solution(id_list, reports, k):
    # 서로 다른 유저 계속 신고 가능
    # 동일 유저에 대한 신고 횟수는 1회로 처리
    # k번 이상 신고된 유저는 게시판 이용 정지, 해당 유저를 신고한 유저에게 메일 발송
    # 유저 신고 내용은 한번에 취합해서 마지막에 메일 발송
    
    # 유저가 신고당한 횟수를 저장하는 딕셔너리
    report_count = {name:0 for name in id_list}
    
    # 유저가 신고한 목록을 저장하는 딕셔너리
    report_log = {name:[] for name in id_list}
    
    # 유저가 받은 메일 수를 저장하는 딕셔너리
    mail = {name:0 for name in id_list}
    
    # 게시판 정지 여부를 저장하는 딕셔너리
    suspended = {name:False for name in id_list}
    
    for report in reports:
        reporter, reported = report.split()
        # 신고자의 신고목록에 피신고자가 없다면 추가하고 피신고자가 신고당한 횟수 1 증가
        if reported not in report_log[reporter]:
            report_log[reporter].append(reported)
            report_count[reported] += 1
            
    # 신고당한 횟수를 검사하여 k이상인 유저의 게시판 정지
    for name, count in report_count.items():
        if count >= k:
            suspended[name] = True
            
    # 정지당한 유저 목록을 검사하여 해당 유저를 신고한 유저의 메일 수 증가
    for name, tf in suspended.items():
        if tf == True:
            for reporter in report_log.keys():
                if name in report_log[reporter]:
                    mail[reporter] += 1
                    
    return [val for val in mail.values()]

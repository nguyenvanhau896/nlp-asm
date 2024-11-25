DATABASE = {
    "TOUR": [
        {"code": "PQ", "name": "Phú Quốc"},
        {"code": "DN", "name": "Đà Nẵng"},
        {"code": "NT", "name": "Nha Trang"}
    ],
    "DTIME": [
        {"code": "PQ", "departure": "HCMC", "time": "7AM 1/7"},
        {"code": "PQ", "departure": "HCMC", "time": "8AM 5/7"},
        {"code": "DN", "departure": "HCMC", "time": "7AM 1/7"},
        {"code": "DN", "departure": "HCMC", "time": "7AM 4/7"},
        {"code": "NT", "departure": "HCMC", "time": "7AM 1/7"},
        {"code": "NT", "departure": "HCMC", "time": "7AM 5/7"}
    ],
    "ATIME": [
        {"code": "PQ", "arrival": "PQ", "time": "9AM 1/7"},
        {"code": "PQ", "arrival": "PQ", "time": "10AM 5/7"},
        {"code": "DN", "arrival": "DN", "time": "9AM 1/7"},
        {"code": "DN", "arrival": "DN", "time": "9AM 4/7"},
        {"code": "NT", "arrival": "NT", "time": "12AM 1/7"},
        {"code": "NT", "arrival": "NT", "time": "12AM 5/7"}
    ],
    "RUN_TIME": [
        {"from": "HCMC", "to": "PQ", "duration": "2:00 HR"},
        {"from": "HCMC", "to": "DN", "duration": "2:00 HR"},
        {"from": "HCMC", "to": "NT", "duration": "5:00 HR"}
    ],
    "BY": [
        {"code": "PQ", "method": "airplane"},
        {"code": "DN", "method": "airplane"},
        {"code": "NT", "method": "train"}
    ]
}

SEM_MAPPING = {
    "HCMC": "Hồ_Chí_Minh",
    "PQ": "Phú_Quốc",
    "NT": "Nha_Trang",
    "DN": "Đà_Nẵng",
    "REMIND1": "nhắc_lại",
    "LIST1": "tất_cả",
    "TRAVEL1": "đi",
    "TRAVEL2": "đi",
    "HOW1": "hết_bao_lâu",
    "HOW2": "có_bao_nhiêu",
    "WHICH1": "bằng_phương_tiện_gì",
    "WHAT1": "có_những_ngày_nào",
    "TOUR1": "tour",
    "EM": "em",
    "ANH": "anh"
}

ENGLISH_TO_VIETNAMESE = {
    "train": "tàu_hỏa",
    "airplane": "máy_bay",
    "bus": "xe_bus"
}

def retrive_data(procedure):
    answer = ""
    tour_list = DATABASE["DTIME"]
    if procedure.type == "LIST1":
        # Get list of tours
        answer += f"Có tất cả {len(tour_list)} tours\nDanh sách các tour:\n"
        for idx, tour in enumerate(tour_list, 1):
            answer += f"Tour {idx} có mã là {tour['code']}, xuất phát từ {SEM_MAPPING[tour['departure']]}, khởi hành lúc {tour['time']}\n"
    elif procedure.type == "HOW1":
        # Get how-long
        source = procedure.source
        dest = procedure.dest
        
        time = None
        for runtime in DATABASE["RUN_TIME"]:
            if runtime['from'] == source and runtime['to'] == dest:
                time = runtime['duration']
                break
        if not time:
            return "Không tìm thấy thời gian đi"    
        answer += f"Đi từ {SEM_MAPPING[source]} tới {SEM_MAPPING[dest]} hết: {time}\n"
    elif procedure.type == "HOW2":
        tour_code = procedure.tour_code
        count = 0
        for tour in tour_list:
            if tour['code'] == tour_code:
                count += 1
        answer = f"Có tất cả {count} tours đi {SEM_MAPPING[tour_code]}\n"    
    elif procedure.type == "WHICH1":
        tour_code = procedure.tour_code
        method = None
        for by in DATABASE["BY"]:
            if by['code'] == tour_code:
                method = by['method']
                break
        if not method:
            return "Không tìm thấy phương tiện di chuyển"
        answer += f"Tour {SEM_MAPPING[tour_code]} đi bằng phương tiện: {ENGLISH_TO_VIETNAMESE[method]}\n"
    elif procedure.type == "WHAT1":
        tour_code = procedure.tour_code
        count = 0
        for tour in tour_list:
            if tour['code'] == tour_code:
                answer += f"Tour {SEM_MAPPING[tour_code]} có ngày khởi hành vào lúc {tour['time']}\n"
    return answer if answer != "" else "Không tìm thấy thông tin"
            
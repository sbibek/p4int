paths = {
    1: {
        2: [(1,7), (7,2)],
        3: [(1,7), (7,10), (10, 9), (9, 3)],
        4: [(1,7), (7,10), (10, 9), (9,4)],
        5: [(1, 7), (7,8), (8, 5)],
        6: [(1,7), (7,8), (8,6)],
        7: [(1,7), (7,10), (10, 11)],
        8: [(1,7), (7,10), (10, 12)]
    },

    2: {
        1: [(2,7), (7,1)],
        3: [(2,7), (7,10), (10, 9), (9,3)],
        4: [(2,7), (7, 10), (10, 9), (9,4)],
        5: [(2,7), (7, 8), (8,5)],
        6: [(2,7), (7,8), (8,6)],
        7: [(2, 7), (7, 10), (10, 11)],
        8: [(2, 7), (7, 10), (10, 12)],
    },

    3: {
        1: [(3,9), (9,10), (10, 7), (7,1)],
        2: [(3,9), (9,10), (10,7), (7,2)],
        4: [(3,9), (9,4)],
        5: [(3,9), (9,8), (8,5)],
        6: [(3,9), (9, 8), (8,6)],
        7: [(3,9), (9, 10), (10, 11)],
        8: [(3,9), (9, 10), (10, 12)]
    },

    4: {
        1: [(4,9), (9,10), (10, 7), (7,1)],
        2: [(4,9), (9,10), (10,7), (7,2)],
        3: [(4,9), (9,3)],
        5: [(4,9), (9,8), (8,5)],
        6: [(4,9), (9, 8), (8,6)],
        7: [(4,9), (9, 10), (10, 11)],
        8: [(4,9), (9, 10), (10, 12)]
    },

    5: {
        1: [(5,8), (8,7), (7,1)],
        2: [(5,8), (8,7), (7,2)],
        3: [(5,8), (8,9), (9,3)],
        4: [(5,8), (8,9), (9,4)],
        6: [(5,8), (8,6)],
        7: [(5,8), (8,7), (7,10), (10, 11)],
        8: [(5,8), (8,7), (7,10), (10, 12)]
    }, 

    6: {
        1: [(6,8), (8,7), (7,1)],
        2: [(6,8), (8,7), (7,2)],
        3: [(6,8), (8,9), (9,3)],
        4: [(6,8), (8,9), (9,4)],
        5: [(6,8), (8,5)],
        7: [(6,8), (8,7), (7,10), (10, 11)],
        8: [(6,8), (8,7), (7,10), (10, 12)]
    },
    7: {
        1: [(11, 10), (10,7), (7,1)],
        2: [(11, 10), (10,7), (7,2)],
        3: [(11, 10), (10, 9), (9, 3)],
        4: [(11, 10), (10,9), (9,4)],
        5: [(11, 10), (10,9), (9,8), (8,5)],
        6: [(11, 10), (10, 9), (9,8), (8,6)],
        8: [(11, 10),(10,12)]
    },
    8: {
        1: [(12, 10), (10,7), (7,1)],
        2: [(12, 10), (10,7), (7,2)],
        3: [(12, 10), (10, 9), (9, 3)],
        4: [(12, 10), (10,9), (9,4)],
        5: [(12, 10), (10,9), (9,8), (8,5)],
        6: [(12, 10), (10, 9), (9,8), (8,6)],
        8: [(12, 10),(10,11)]
    }
}


pathsWithEgress = {
    1: {
        2: (1, 2, 7, 4, 2, 1),
        3: (1,2, 7, 2 ,10,2, 9, 3, 3, 1),
        4: (1,2, 7,2,10,2, 9,4,4),
        5: (1,2, 7,1,8,4, 5,1),
        6: (1,2,7,1,8,3,6,1),
        7: (1,2,7,2,10,3, 11,1),
        8: (1,2,7,2,10,4, 12,1)
    },

    2: {
        1: (2,2,7,3,1,1),
        3: (2,2,7,2,10,2,9,3,3,1),
        4: (2,2,7,2, 10,2, 9,4,4,1),
        5: (2,2,7,1, 8,4,5,1),
        6: (2,2,7,1,8,3,6,1),
        7: (2,2,7,2, 10,3, 11,1),
        8: (2,2,7,2, 10,4, 12,1),
    },

    3: {
        1: (3,2,9,1,10,1, 7,3,1,1),
        2: (3,2,9,1,10,1,7,4,2,1),
        4: (3,2,9,4,4,1),
        5: (3,2,9,2,8,4,5,1),
        6: (3,2,9,2, 8,3,6,1),
        7: (3,2,9,1, 10,3, 11,1),
        8: (3,2,9,1, 10,4, 12,1)
    },

    4: {
        1: (4,2,9,1,10,1, 7,3,1,1),
        2: (4,2,9,1,10,1,7,4,2,1),
        3: (4,2,9,3,3,1),
        5: (4,2,9,2,8,4,5,1),
        6: (4,2,9,2, 8,3,6,1),
        7: (4,2,9,1, 10,3, 11,1),
        8: (4,2,9,1, 10,4, 12,1)
    },

    5: {
        1: (5,2,8,2,7,3,1),
        2: (5,2,8,2,7,4,2,1),
        3: (5,2,8,1,9,3,3,1),
        4: (5,2,8,1,9,4,4,1),
        6: (5,2,8,3,6,1),
        7: (5,2,8,2,7,2,10,3, 11,1),
        8: (5,2,8,2,7,2,10,4, 12, 1)
    }, 

    6: {
        1: (6,2,8,2,7,3,1),
        2: (6,2,8,2,7,4,2,1),
        3: (6,2,8,1,9,3,3,1),
        4: (6,2,8,1,9,4,4,1),
        5: (6,2,8,4,5,1),
        7: (6,2,8,2,7,2,10,3, 11,1),
        8: (6,2,8,2,7,2,10,4, 12, 1)
    },
    7: {
        1: (11,2, 10,1,7,3,1,1),
        2: (11,2, 10,1,7,4,2,1),
        3: (11,2, 10,2, 9,3, 3,1),
        4: (11,2, 10,2,9,4,4,1),
        5: (11,2, 10,2,9,2,8,4,5,1),
        6: (11,2, 10,2, 9,2,8,3,6,1),
        8: (11,2, 10,4,12,1)
    },
    8: {
        1: (12,2, 10,1,7,3,1,1),
        2: (12,2, 10,1,7,4,2,1),
        3: (12,2, 10,2, 9,3, 3,1),
        4: (12,2, 10,2,9,4,4,1),
        5: (12,2, 10,2,9,2,8,4,5,1),
        6: (12,2, 10,2, 9,2,8,3,6,1),
        7: (12,2, 10,3,11,1)
    }
}

# { hop:{egress_port:bandwidth}}
bandwidthf = {
    1:{1:8, 2:8, 3:8, 4:8},
    2:{1:7, 2:7, 3:7, 4:7},
    3:{1:5, 2:5, 3:5, 4:5},
    4:{1:8, 2:8, 3:8, 4:8},
    5:{1:7, 2:7, 3:7, 4:7},
    6:{1:8, 2:8, 3:8, 4:8},
    7:{1:8, 2:8, 3:8, 4:8},
    8:{1:6, 2:6, 3:6, 4:6},
    9:{1:8, 2:8, 3:8, 4:8},
    10:{1:8, 2:8, 3:8, 4:8},
    11:{1:5, 2:5, 3:5, 4:5},
    12:{1:5, 2:5, 3:5, 4:5}
}

nstate = {
    "hop": {
        1: {"hoplatency": 0},
                1: {"hoplatency": 1},
                2: {"hoplatency": 2},
                3: {"hoplatency": 3},
                4: {"hoplatency": 4},
                5: {"hoplatency": 5},
                6: {"hoplatency": 6}
    },
    "link": {
        "1->2": {"max": 10 },
        "4->6": {"max": 11 },
        "3->6": {"max": 12 },
        "2->3": {"max": 13 },
        "5->4": {"max": 14 },
        "2->5": {"max": 15 }
    }
}
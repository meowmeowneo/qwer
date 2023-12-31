import pprint as pp
import pandas as pd
import copy

dict_week_disciplines = {
    'monday':{
        1:{},
        2:{},
        3:{},
        4:{},
        5:{}
        },
    'tuesday':{
        1:{},
        2:{},
        3:{},
        4:{},
        5:{}
        },
    'wednsday':{
        1:{},
        2:{},
        3:{},
        4:{},
        5:{}
        },
    'thursday':{
        1:{},
        2:{},
        3:{},
        4:{},
        5:{}
        },
    'friday':{
        1:{},
        2:{},
        3:{},
        4:{},
        5:{}
        }
}

dict_week_teachers = {
    'monday':{
        1:{},
        2:{},
        3:{},
        4:{},
        5:{}
        },
    'tuesday':{
        1:{},
        2:{},
        3:{},
        4:{},
        5:{}
        },
    'wednsday':{
        1:{},
        2:{},
        3:{},
        4:{},
        5:{}
        },
    'thursday':{
        1:{},
        2:{},
        3:{},
        4:{},
        5:{}
        },
    'friday':{
        1:{},
        2:{},
        3:{},
        4:{},
        5:{}
        }
}

dict_groups_week_workload={1: 36, 2: 35, 3: 43, 4: 34, 5: 34, 6: 34, 7: 41.7, 8: 36, 9: 36, 10: 36, 11: 32, 12: 32, 13: 32, 14: 36, 15: 36, 16: 36, 17: 36, 18: 32, 19: 36, 20: 32, 21: 34, 22: 36, 23: 36, 24: 30, 25: 32, 26: 32, 27: 32, 28: 36, 29: 36, 30: 36, 31: 36, 32: 36.0}

# dict_sorted_groups_week_workload = dict(sorted(dict_groups_week_workload.items(),key= lambda x:x[1], reverse=True))
dict_sorted_groups_week_workload = {3: 43, 7: 41.7, 1: 36, 8: 36, 9: 36, 10: 36, 14: 36, 15: 36, 16: 36, 17: 36, 19: 36, 22: 36, 23: 36, 28: 36, 29: 36, 30: 36, 31: 36, 32: 36.0, 2: 35, 4: 34, 5: 34, 6: 34, 21: 34, 11: 32, 12: 32, 13: 32, 18: 32, 20: 32, 25: 32, 26: 32, 27: 32, 24: 30}

dict_teathers_workload={20: 38, 11: 39.4, 25: 32, 29: 47, 2: 44.0, 21: 55, 33: 40.1, 10: 37.7, 9: 40, 23: 26, 34: 44, 6: 31.4, 13: 34, 3: 23, 30: 14, 32: 37, 14: 42, 5: 33, 26: 7.3, 22: 44, 12: 42, 16: 39, 28: 36.2, 4: 35, 17: 24.9, 1: 39.3, 24: 6, 7: 39, 27: 48, 15: 19, 18: 14, 19: 17, 8: 6, 31: 19.1}

# sorted_teacherts_workload_dict = dict(sorted(dict_teathers_workload.items(), key=lambda x: x[1], reverse=True))
dict_sorted_teacherts_workload = {21: 55, 27: 48, 29: 47, 2: 44.0, 34: 44, 22: 44, 14: 42, 12: 42, 33: 40.1, 9: 40, 11: 39.4, 1: 39.3, 16: 39, 7: 39, 20: 38, 10: 37.7, 32: 37, 28: 36.2, 4: 35, 13: 34, 5: 33, 25: 32, 6: 31.4, 23: 26, 17: 24.9, 3: 23, 31: 19.1, 15: 19, 19: 17, 30: 14, 18: 14, 26: 7.3, 24: 6, 8: 6}

dict_groups_teachers = {1: [2, 10, 11, 20, 21, 25, 29, 31, 33], 2: [9, 10, 11, 20, 29], 3: [3, 5, 6, 9, 13, 14, 23, 26, 30, 32, 33, 34], 4: [5, 10, 12, 13, 16, 20, 22, 28, 32, 34], 5: [4, 11, 16, 17, 20, 21, 29], 6: [9, 11, 20, 21, 25], 7: [1, 2, 6, 10, 11, 28, 33], 8: [2, 5, 7, 16, 20, 22, 24, 27, 28, 29, 33], 9: [1, 2, 7, 11, 16, 20, 22, 27, 28, 29, 33], 10: [1, 2, 7, 11, 16, 20, 22, 27, 28, 29, 33], 11: [11, 14, 20, 22, 25, 27, 29, 33], 12: [11, 14, 20, 22, 25, 27, 
29, 33], 13: [11, 14, 20, 22, 25, 27, 29, 33], 14: [1, 11, 15, 18, 20, 21, 25], 15: [11, 14, 15, 18, 19, 20, 21, 28], 16: [1, 8, 9, 11, 14, 20, 25, 27], 17: [1, 4, 5, 6, 7, 9, 13, 17, 19, 31], 18: [2, 5, 6, 9, 10, 13, 14, 16, 23, 28], 19: [1, 4, 7, 9, 11, 13, 14, 17, 19, 20], 20: [2, 5, 6, 9, 10, 13, 14, 16, 23, 28], 21: [4, 11, 12, 20, 25], 22: [3, 5, 6, 7, 12, 17, 22, 29, 31, 32, 34], 23: [7, 11, 12, 14, 20, 25], 24: [3, 5, 6, 9, 12, 32, 34], 25: [2, 5, 6, 8, 13, 16, 21, 24, 28, 32], 26: [1, 2, 5, 6, 10, 16, 22, 28, 33], 27: [1, 2, 5, 10, 16, 20, 22, 28, 33], 28: [3, 6, 7, 11, 12, 17, 22, 29, 31, 32, 34], 29: [3, 5, 6, 7, 13, 14, 23, 26, 30, 32, 34], 30: [3, 5, 6, 
7, 13, 14, 23, 26, 30, 32, 34], 31: [3, 5, 6, 7, 13, 23, 26, 30, 32, 34], 32: [3, 5, 6, 13, 14, 23, 26, 32, 33, 34]}

# for group in dict_groups_teachers:
#     for i in range(0, len(dict_groups_teachers[group])-1):
#         for j in range(0, len(dict_groups_teachers[group])-1):
#             if dict_sorted_teacherts_workload[dict_groups_teachers[group][j]]<dict_sorted_teacherts_workload[dict_groups_teachers[group][j+1]]:
#                 d=dict_groups_teachers[group][j]
#                 dict_groups_teachers[group][j]=dict_groups_teachers[group][j+1]
#                 dict_groups_teachers[group][j+1]=d
dict_sorted_groups_teachers = {1: [21, 29, 2, 33, 11, 20, 10, 25, 31], 2: [29, 9, 11, 20, 10], 3: [34, 14, 33, 9, 32, 13, 5, 6, 23, 3, 30, 26], 4: [22, 34, 12, 16, 20, 10, 32, 28, 13, 5], 5: [21, 29, 11, 16, 20, 4, 17], 6: [21, 9, 11, 20, 25], 7: [2, 33, 
11, 1, 10, 28, 6], 8: [27, 29, 2, 22, 33, 7, 16, 20, 28, 5, 24], 9: [27, 29, 2, 22, 33, 11, 1, 7, 16, 20, 28], 10: [27, 29, 2, 22, 33, 11, 1, 7, 16, 20, 28], 11: [27, 29, 22, 14, 33, 11, 20, 25], 12: [27, 29, 22, 14, 33, 11, 
20, 25], 13: [27, 29, 22, 14, 33, 11, 20, 25], 14: [21, 11, 1, 20, 25, 15, 18], 15: [21, 14, 11, 20, 28, 15, 19, 18], 16: [27, 14, 9, 11, 1, 20, 25, 8], 17: [9, 1, 7, 4, 13, 5, 6, 17, 31, 19], 18: [2, 14, 9, 16, 10, 28, 13, 5, 6, 23], 19: [14, 9, 11, 1, 7, 20, 4, 13, 17, 19], 20: [2, 14, 9, 16, 10, 28, 13, 5, 6, 23], 21: [12, 11, 20, 4, 25], 22: [29, 22, 34, 12, 7, 32, 5, 6, 17, 3, 31], 23: [12, 14, 11, 7, 20, 25], 24: [34, 12, 9, 32, 5, 6, 3], 25: [21, 2, 16, 32, 28, 13, 5, 6, 8, 24], 26: [2, 22, 33, 1, 16, 10, 28, 5, 6], 27: [2, 22, 33, 1, 16, 20, 10, 28, 5], 28: [29, 22, 34, 12, 11, 7, 32, 6, 17, 3, 31], 29: [34, 14, 7, 32, 13, 5, 6, 23, 3, 30, 26], 30: [34, 14, 7, 32, 13, 5, 6, 23, 3, 30, 26], 31: [34, 7, 32, 13, 5, 6, 23, 3, 30, 26], 32: [34, 14, 33, 32, 13, 5, 6, 23, 3, 26]}

dict_groups_disciplines_hour_per_week={1: {29: 6, 33: 7, 40: 3, 47: 5, 49: 4, 60: 2, 120: 3, 166: 3, 168: 3}, 2: {40: 8, 49: 11, 50: 5, 56: 5, 166: 3, 168: 3}, 3: {1: 1, 9: 2, 10: 2, 11: 2, 12: 1, 150: 1, 151: 3, 152: 6, 153: 1, 154: 3, 155: 2, 156: 1, 157: 1, 158: 4, 159: 2, 160: 8, 161: 2, 162: 1}, 4: {13: 2, 16: 2, 30: 4, 69: 5, 71: 2, 75: 2, 83: 2, 88: 2, 92: 3, 98: 2, 102: 4, 116: 4}, 5: {25: 7, 30: 5, 32: 6, 34: 6, 41: 6, 71: 2, 75: 2}, 6: {41: 9, 51: 8, 57: 8, 71: 2, 75: 2, 106: 5}, 7: {14: 2.2, 35: 3.6, 67: 5.8, 69: 3.3, 76: 4.4, 79: 4.4, 133: 3.1, 134: 4.4, 135: 2.7, 163: 4.9, 164: 2.9}, 8: {14: 3, 61: 5, 62: 4, 63: 4, 64: 3, 65: 3, 72: 3, 77: 2, 79: 2, 117: 3, 124: 2, 132: 2}, 9: {14: 3, 61: 5, 62: 4, 63: 4, 64: 3, 65: 3, 72: 3, 77: 2, 79: 2, 117: 3, 124: 2, 132: 2}, 10: {14: 3, 61: 5, 62: 4, 63: 4, 64: 3, 65: 3, 72: 3, 77: 2, 79: 2, 117: 3, 124: 2, 132: 2}, 11: {36: 2, 42: 2, 52: 7, 58: 3, 59: 4, 77: 2, 79: 2, 103: 2, 121: 3, 126: 3, 132: 2}, 12: {36: 2, 42: 2, 52: 7, 58: 3, 59: 4, 77: 2, 79: 2, 103: 2, 121: 3, 126: 3, 132: 2}, 13: {36: 2, 42: 2, 52: 7, 58: 3, 59: 4, 77: 2, 79: 2, 103: 2, 121: 3, 126: 3, 132: 2}, 14: {24: 6, 43: 6, 48: 4, 53: 9, 69: 3, 73: 2, 75: 2, 107: 2, 129: 2}, 15: {13: 1, 24: 2, 26: 5, 31: 2, 43: 2, 48: 2, 53: 3, 73: 2, 75: 2, 93: 5, 104: 3, 107: 3, 112: 2, 125: 2}, 16: {2: 3, 21: 5, 23: 2, 37: 3, 44: 3, 84: 3, 141: 4, 165: 4, 167: 
2, 168: 3, 170: 4}, 17: {22: 6, 89: 3, 94: 3, 99: 3, 105: 3, 113: 4, 118: 4, 165: 6, 167: 2, 169: 2}, 18: {18: 2, 27: 5, 77: 2, 79: 2, 82: 2, 87: 6, 96: 4, 101: 5, 109: 2, 130: 2}, 19: {22: 6, 89: 2, 99: 3, 105: 2, 114: 3, 119: 5, 141: 6, 165: 5, 167: 2, 169: 2}, 20: {18: 2, 27: 5, 77: 2, 79: 2, 82: 2, 87: 6, 96: 4, 101: 5, 109: 2, 130: 2}, 21: {38: 7, 45: 7, 54: 8, 108: 5, 167: 2, 169: 2, 170: 3}, 22: {13: 4, 17: 3, 28: 6, 69: 4, 73: 2, 75: 2, 85: 6, 95: 6, 131: 3}, 23: {39: 5, 46: 8, 55: 6, 73: 2, 75: 2, 110: 6, 122: 4, 127: 3}, 24: {13: 4, 20: 4, 70: 3, 71: 2, 75: 2, 86: 5, 91: 5, 111: 5}, 25: {15: 5, 18: 3, 70: 3, 71: 2, 75: 2, 80: 3, 87: 2, 90: 2, 96: 2, 123: 3, 128: 5}, 26: {15: 2, 19: 2, 68: 3, 74: 3, 78: 2, 81: 2, 87: 4, 90: 4, 97: 3, 100: 3, 115: 4}, 27: {15: 2, 19: 2, 68: 3, 74: 3, 78: 2, 81: 2, 87: 4, 90: 4, 97: 3, 100: 3, 115: 4}, 28: {13: 4, 17: 3, 28: 6, 69: 4, 73: 2, 75: 2, 85: 6, 95: 6, 131: 3}, 29: {3: 1, 136: 2, 137: 3, 138: 3, 139: 2, 140: 2, 141: 2, 142: 2, 143: 2, 144: 3, 145: 1, 147: 6, 148: 4, 149: 3}, 30: {3: 1, 136: 2, 137: 3, 138: 3, 139: 2, 140: 2, 141: 2, 142: 2, 143: 2, 144: 3, 145: 1, 147: 6, 148: 4, 149: 3}, 31: {136: 3, 137: 3, 138: 2, 139: 2, 142: 2, 143: 2, 144: 3, 145: 2, 146: 3, 147: 7, 148: 3, 149: 4}, 32: {4: 4, 5: 4, 6: 2, 7: 2, 8: 3.7, 66: 1, 150: 2, 152: 5, 153: 2, 154: 3, 155: 1, 158: 2, 161: 2, 162: 2.3}}

# for discipline in dick_groups_disciplines_hour_per_week:
#     dict_groups_disciplines_hour_per_week[discipline]=dict(sorted(dict_groups_disciplines_hour_per_week[discipline].items(), key=lambda x:x[1], reverse=True))
dict_sorted_groups_disciplines_hour_per_week={1: {33: 7, 29: 6, 47: 5, 49: 4, 40: 3, 120: 3, 166: 3, 168: 3, 60: 2}, 2: {49: 11, 40: 8, 50: 5, 56: 5, 166: 3, 168: 3}, 3: {160: 8, 152: 6, 158: 4, 151: 3, 154: 3, 9: 2, 10: 2, 11: 2, 155: 2, 159: 2, 161: 2, 1: 1, 12: 1, 150: 1, 153: 1, 156: 1, 157: 1, 162: 1}, 4: {69: 5, 30: 4, 102: 4, 116: 4, 92: 3, 13: 2, 16: 2, 71: 2, 75: 2, 83: 2, 88: 2, 98: 2}, 5: {25: 7, 32: 6, 34: 6, 41: 6, 30: 5, 71: 2, 75: 2}, 6: {41: 9, 51: 8, 57: 8, 106: 5, 71: 2, 75: 2}, 7: {67: 5.8, 163: 4.9, 76: 4.4, 79: 4.4, 134: 4.4, 35: 3.6, 69: 3.3, 133: 3.1, 164: 2.9, 135: 2.7, 14: 2.2}, 8: {61: 5, 62: 4, 63: 4, 14: 3, 64: 3, 65: 3, 72: 3, 117: 3, 77: 2, 79: 2, 124: 2, 132: 2}, 9: {61: 5, 62: 4, 63: 4, 14: 3, 64: 3, 65: 3, 72: 3, 117: 3, 77: 2, 79: 2, 124: 2, 132: 2}, 10: {61: 5, 62: 4, 63: 4, 14: 3, 64: 3, 65: 3, 72: 3, 117: 3, 77: 2, 79: 2, 124: 2, 132: 2}, 11: {52: 7, 59: 4, 58: 3, 121: 3, 126: 3, 36: 2, 42: 2, 77: 2, 79: 2, 103: 2, 132: 2}, 12: {52: 7, 59: 4, 58: 3, 121: 3, 126: 3, 36: 2, 42: 2, 77: 2, 79: 2, 103: 2, 132: 2}, 13: {52: 7, 59: 4, 58: 3, 121: 3, 126: 3, 36: 2, 42: 2, 77: 2, 79: 2, 103: 2, 132: 2}, 14: {53: 9, 24: 6, 43: 6, 48: 4, 69: 3, 73: 2, 75: 2, 107: 2, 129: 2}, 15: {26: 5, 93: 5, 53: 3, 104: 3, 107: 3, 24: 2, 31: 2, 43: 2, 48: 2, 73: 2, 75: 2, 112: 2, 125: 2, 13: 1}, 16: {21: 5, 141: 4, 165: 4, 170: 4, 2: 3, 37: 3, 44: 3, 84: 3, 168: 3, 23: 2, 167: 2}, 17: {22: 6, 165: 6, 113: 4, 118: 4, 89: 3, 94: 3, 99: 3, 105: 3, 167: 2, 169: 2}, 18: {87: 6, 27: 5, 101: 5, 96: 4, 18: 2, 77: 2, 79: 2, 82: 2, 109: 2, 130: 2}, 19: {22: 6, 141: 6, 119: 5, 165: 5, 99: 3, 114: 3, 89: 2, 105: 2, 167: 2, 169: 2}, 20: {87: 6, 27: 5, 101: 5, 96: 4, 18: 2, 77: 2, 79: 2, 82: 2, 109: 2, 130: 2}, 21: {54: 8, 38: 7, 45: 7, 108: 5, 170: 3, 167: 2, 169: 2}, 22: {28: 6, 85: 6, 95: 6, 13: 4, 69: 4, 17: 3, 131: 3, 73: 2, 75: 2}, 23: {46: 8, 55: 6, 110: 6, 39: 5, 122: 4, 127: 3, 73: 2, 75: 2}, 24: {86: 5, 91: 5, 111: 5, 13: 4, 20: 4, 70: 3, 71: 2, 75: 2}, 25: {15: 5, 128: 5, 18: 3, 70: 3, 80: 3, 123: 3, 71: 2, 75: 2, 87: 2, 90: 2, 96: 2}, 26: {87: 4, 90: 4, 115: 4, 68: 3, 74: 3, 97: 3, 100: 3, 15: 2, 19: 2, 78: 2, 81: 2}, 27: {87: 4, 90: 4, 115: 4, 68: 3, 74: 3, 97: 3, 100: 3, 15: 2, 19: 2, 78: 2, 81: 2}, 28: {28: 6, 85: 6, 95: 6, 13: 4, 69: 4, 17: 3, 131: 3, 73: 2, 75: 2}, 29: {147: 6, 148: 4, 137: 3, 138: 3, 144: 3, 149: 3, 136: 2, 139: 2, 140: 2, 141: 2, 142: 2, 143: 2, 3: 1, 145: 1}, 30: {147: 6, 148: 4, 137: 3, 138: 3, 144: 3, 149: 3, 136: 2, 139: 2, 140: 2, 141: 2, 142: 2, 143: 2, 3: 1, 145: 1}, 31: {147: 7, 149: 4, 136: 3, 137: 3, 144: 3, 146: 3, 148: 3, 138: 2, 139: 2, 142: 2, 143: 2, 145: 2}, 32: {152: 5, 4: 4, 5: 4, 8: 3.7, 154: 3, 162: 2.3, 6: 2, 7: 2, 150: 2, 153: 2, 158: 2, 161: 2, 66: 1, 155: 1}}

dict2 = copy.deepcopy(dict_sorted_groups_disciplines_hour_per_week)

dict_teachers_disciplines={1: [68, 69, 72, 74, 165], 2: [27, 33, 35, 64, 90, 134], 3: [17, 20, 149, 155], 4: [32, 45, 54, 105, 113, 119], 5: [75, 79, 81, 144, 161, 169], 6: [71, 73, 76, 77, 78, 138, 153, 167], 7: [3, 85, 110, 114, 117, 118, 146], 8: [84, 123], 9: [1, 37, 50, 56, 57, 91, 94, 99, 130], 10: [49, 100, 101, 102, 135], 11: [75, 79, 168, 169], 12: [38, 39, 86, 88, 92, 95, 108, 127], 13: [16, 89, 96, 148, 154], 14: [6, 9, 103, 109, 122, 125, 141, 160], 15: [24, 43, 107], 16: [30, 87, 98, 124], 18: [43, 53], 19: [22, 93], 20: [71, 73, 77, 78, 166, 167], 21: [26, 31, 34, 40, 41, 48, 51, 104, 112, 128], 22: [52, 65, 83, 97, 131], 23: [82, 136, 137, 150, 151], 24: [72, 80], 25: [55, 106, 120, 126, 129, 170], 26: [145, 162], 27: [2, 58, 61, 62, 121], 28: [13, 14, 15, 18, 19, 116], 29: [25, 28, 29, 40, 60, 132], 30: [142, 143, 156, 157], 32: [69, 70, 139, 140, 158, 159], 33: [5, 11, 36, 47, 63, 115, 133], 34: 
[13, 147, 152]}

mdk_dict={1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0, 21: 1, 22: 1, 23: 1, 24: 1, 25: 1, 26: 1, 27: 1, 28: 1, 29: 1, 30: 1, 31: 1, 32: 1, 33: 1, 34: 1, 35: 1, 36: 1, 37: 1, 38: 1, 39: 1, 40: 1, 41: 1, 42: 1, 43: 1, 44: 1, 45: 1, 46: 1, 47: 1, 48: 1, 49: 1, 50: 1, 51: 1, 52: 1, 53: 1, 54: 1, 55: 1, 56: 1, 57: 1, 58: 1, 59: 1, 60: 1, 61: 1, 62: 1, 63: 1, 64: 1, 65: 1, 66: 1, 67: 1, 68: 0, 69: 0, 70: 0, 71: 0, 72: 0, 73: 0, 74: 0, 75: 0, 76: 0, 77: 0, 78: 0, 79: 0, 80: 0, 81: 0, 82: 0, 83: 0, 84: 0, 85: 0, 86: 0, 87: 0, 88: 0, 89: 0, 90: 0, 91: 0, 92: 0, 93: 0, 94: 0, 95: 0, 96: 0, 97: 0, 98: 0, 99: 0, 100: 0, 101: 0, 102: 0, 103: 0, 104: 0, 105: 0, 106: 0, 107: 0, 108: 0, 109: 0, 110: 0, 111: 0, 112: 0, 113: 0, 114: 0, 115: 0, 116: 0, 117: 0, 118: 0, 119: 0, 120: 0, 121: 0, 122: 0, 123: 0, 124: 0, 125: 0, 126: 0, 127: 0, 128: 0, 129: 0, 130: 0, 131: 0, 132: 0, 133: 0, 134: 0, 135: 0, 136: 0, 137: 0, 138: 0, 139: 0, 140: 0, 141: 0, 142: 0, 143: 0, 144: 0, 145: 0, 146: 0, 147: 0, 148: 0, 149: 0, 150: 0, 151: 0, 152: 0, 153: 0, 154: 0, 155: 0, 156: 0, 157: 0, 158: 0, 159: 0, 160: 0, 161: 0, 162: 0, 163: 0, 164: 0, 165: 0, 166: 0, 167: 0, 168: 0, 169: 0, 170: 0}

flag = False
for day in dict_week_disciplines:
    dict_day_workload={}
    for pair_number in dict_week_disciplines[day]:
        active_teacher=[]
        for group in dict_sorted_groups_week_workload:
            flag = False
            for teacher in dict_sorted_groups_teachers[group]:
                if teacher not in active_teacher:
                    for discipline in dict_sorted_groups_disciplines_hour_per_week[group]:
                        if teacher in dict_teachers_disciplines and discipline in dict_teachers_disciplines[teacher] and dict2[group][discipline]>0 and (group not in dict_day_workload or len(dict_day_workload[group])<4) and (mdk_dict[discipline]==1 or (group not in dict_day_workload) or (group not in dict_week_disciplines[day][pair_number-1]) or dict_week_disciplines[day][pair_number-1][group]!=discipline):
                            dict_week_disciplines[day][pair_number][group]=discipline
                            dict_week_teachers[day][pair_number][group]=teacher
                            active_teacher.append(teacher)
                            dict2[group][discipline]-=2
                            if group in dict_day_workload:
                                dict_day_workload[group].update({pair_number:1})
                            else:
                                dict_day_workload[group]={pair_number:1}
                            flag = True
                        if flag: break
                    if flag: break

for day in dict_week_disciplines:
    print(day)
    df=pd.DataFrame(dict_week_disciplines[day])
    dfff=df.transpose()
    print(dfff)

# for day in dict_week_disciplines:
#     print(day)
#     df=pd.DataFrame(dict_week_teachers[day])
#     dfff=df.transpose()
#     print(dfff)

# print(dict_day_workload)

print(dict_sorted_groups_disciplines_hour_per_week)
print(dict2)

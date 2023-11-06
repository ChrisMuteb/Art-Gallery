# Participant: Team 5
# Angela Makhanu -- Member
# Carmel Kevin -- Leader
# Stephany Lynn -- Member
# Chris Kayomb -- Member

class Painting:
    def __init__(self, paint_id, paint_type, paint_tag_num, paint_tag_lst):
        self._paint_id = paint_id
        self._paint_type = paint_type
        self._paint_tag_num = paint_tag_num
        self._paint_tag_lst = paint_tag_lst

    def __str__(self):
        return f'{self._paint_id} {self._paint_type} {self._paint_tag_num} {self._paint_tag_lst}'


# read from file
def read_data(file):
    try:
        with open(file, 'r') as my_file:
            lst = my_file.readlines()
            return lst
    except IOError as e:
        print(f"An error occurred: {e}")

# write to a file
def writeData(file, data):
    pass


def categorize_frames(data):
    frame_id = 0
    frame_landscape = []
    frame_portrait = []

    for line in data[1:]:
        line_parts = line.split()
        frame_type = line_parts[0]
        frame_tag_num = int(line_parts[1])
        frame_tag_lst = set(line_parts[2:])
        painting = Painting(frame_id, frame_type, frame_tag_num, frame_tag_lst)

        if frame_type == 'L':
            frame_landscape.append(painting)
        else:
            frame_portrait.append(painting)
        frame_id += 1

    # print("Landscape Frames:", frame_landscape)
    # print("Portrait Frames:", frame_portrait)

    return frame_landscape, frame_portrait

# local robotic satisfaction
def local_robotic_satisfaction(frameglassA, frameglassB):
    inter_result = frameglassA.intersection(frameglassB)
    diff_A = len(frameglassA) - len(inter_result)
    diff_B = len(frameglassB) - len(inter_result)
    return min(len(inter_result), diff_A, diff_B)

# sort painting based on the number of tags in an ascending order
def sort_painting(paintings):
    return sorted(paintings, key=lambda painting: painting._paint_tag_num)

if __name__ == "__main__":
    data = read_data('Data/1_binary_landscapes.txt')
    landscape, portrait = categorize_frames(data)
    landscape_lst = []
    portrait_lst = []

    print("Landscape Frames:")
    for painting in landscape:
        print(painting)
        landscape_lst.append(painting)
    
    print("Portrait Frames:")
    for painting in portrait:
        # print(painting)
        portrait_lst.append(painting)

    # test local_score_function
    # frameAs = portrait_lst[0]._paint_tag_lst
    # frameBs = landscape_lst[0]._paint_tag_lst
    # print(frameAs)
    # print(frameBs)
    # print(local_robotic_satisfaction(frameAs, frameBs))

    # test sort painting based on their tag number
    sorted_landscape = sort_painting(landscape_lst)
    print(sorted_landscape[len(sorted_landscape)-1]._paint_tag_num)
    for painting in sorted_landscape:
        # print(painting)
        
        print(painting)



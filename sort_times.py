

import random as rd                                                                     # importing random
import time as tm                                                                       # importing time
import matplotlib.pyplot as mpl                                                         # importing matplotlib


from sorts import merge_sort, quick_sort, insertion_sort, quick_insertion_sort          # importing a functions from sorts file


                                                                                        # Global arrays which we can call everywhere
SIZES = [200, 500, 800, 1100, 1400, 1700, 2000]


def sort_function_timer(sort_function, an_array):                                       #sort_function_times


    start_time = tm.time()
    sort_function(an_array)
    end_time = tm.time()
    return end_time - start_time



def generate_random_array(size):                                                        #generation random arrays



    # return [rd.randint(0, 1000) for _ in range(size)]

                                                                                        #two ways how to generate randon arrays

    random_numbers = []
    for _ in range(size):
        random_number = rd.randint(0, 1000)
        random_numbers.append(random_number)
    return random_numbers



'''1# def generate_sorted_array(size):                                                   # generate sorted arrays func
#     return list(range(size))'''


def plot_sort_time_using_random_arrays(sort_function):                                  #plot_sort_times_unisg_randon_arrays


    print("timing", sort_function.__name__)
    times = []

    for size in SIZES:
        arr = generate_random_array(size)
        elapsed_time = sort_function_timer(sort_function, arr)
        times.append(elapsed_time)
    mpl.plot(SIZES, times, label=sort_function.__name__)



def plot_sort_time_using_sorted_arrays(sort_function):                                  #plot_sort_time_using_sorted_arrays
    print("timing", sort_function.__name__)
    times = []
    for size in SIZES:
        arr = list(range(size))
        elapsed_time = sort_function_timer(sort_function, arr)
        times.append(elapsed_time)
    mpl.plot(SIZES, times, label=sort_function.__name__)


'''   1 # print("timing", sort_function.__name__)
    # times = []
    # 
    # for size in SIZES:
    #     arr = generate_sorted_array(size)
    #     elapsed_time = sort_function_timer(sort_function, arr)
    #     times.append(elapsed_time)
    # 
    # mpl.plot(SIZES, times, label=sort_function.__name__)'''


def main():                                                                             #main function




    mpl.figure()                                                                        # creating a figure
                                                                                        # Test 1: Compare insertion_sort, merge_sort,
                                                                                        # and quick_insertion_sort with using some random arrays

    plot_sort_time_using_random_arrays(insertion_sort)                                  # using an insertion_sort function with random array
    plot_sort_time_using_random_arrays(merge_sort)                                      # using a merge_sort function with random array
    plot_sort_time_using_random_arrays(quick_insertion_sort)                            # using a quick_insertion_sort function with random array
    plot_sort_time_using_random_arrays(quick_sort)                                      # using a quick_sort function with random array


    mpl.title("Random Arrays")                                                          # writing a title
    mpl.xlabel("Array Size")                                                            # writing on x-axis
    mpl.ylabel("Time (seconds)")                                                        # writing on y-axis
    mpl.legend()                                                                        # inscriptions and writing graphics
    mpl.show()                                                                          # demonstration


                                                                                        # Test 2: Compare insertion_sort, merge_sort,
                                                                                        # and quick_insertion_sort with some using sorted arrays
    mpl.figure()
    plot_sort_time_using_sorted_arrays(insertion_sort)                                  # using an insertion_sort function with sorted array
    plot_sort_time_using_sorted_arrays(merge_sort)                                      # using a merge_sort function with sorted array
    plot_sort_time_using_sorted_arrays(quick_insertion_sort)                            # using a quick_insertion_sort function with sorted array
    plot_sort_time_using_sorted_arrays(quick_sort)                                      # using a quick_sort function with sorted array

    mpl.title("Sorted Arrays")                                                          # writing a title
    mpl.xlabel("Array Size")                                                            # writing on x-axis
    mpl.ylabel("Time (seconds)")                                                        # writing on y-axis
    mpl.legend()                                                                        # inscriptions and writing graphics
    mpl.show()                                                                          # demonstration
main()

















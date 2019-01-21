NAME: HEERA SRIDHAR
UTA ID: 1001529609
PROGRAMMING LANGUAGE: Python
 
DESCRIPTION: 
                        The algorithm used to find the shortest path from source to destination is uniform cost search. Uniform cost search finds the shortest path by adding the minimum metrics needed to reach a goal. 

STRUCTURE OF THE CODE:
     1. Class PriorityQueue: The PriorityQueue data structure is used. Here def _put does Heappush (inserts elements in queue) and     def _get does heappop pops elements from queue.
     2. Create_graph function reads the input1.txt file and variables s,d,cost stores the value of the distance/cost from cityA to    City B .
                   For ex: 
                   Luebeck Hamburb 63 
                   Hamberb Bremen 116 .....
                   Like the above example it stores all the possible cities path cost from one city to another.
     3. Uniform _cost _Search function does the following:
         1.Checks if the source or destination is present or absent in the graph,if queue is empty the output is as follows:
             distance: infinity
             route: 
             none
         2. If a path exists from the given source to goal the paths are displayed with the distance/cost value along the path with the total cost of the path.
             The values are stored like this:
             For example: city S to A to B to C to D totalcost.
     4. Class disp_path displays the total distance from source to goal and paths needed to reach the goal with its cost.
     For Ex:
        distance: 455 km
        route: 
        Bremen to Dortmund, 234 km 
        Dortmund to Frankfurt, 221 km 

HOW TO RUN THE CODE:

       1. The input1.txt has the name of the cities and path distance as:
                            CITY-A   CITY-B   metric.
       2. Only when the input.txt file is in this format the code works.
       3. Open a compiler in which change the path to the folder path and compile using  "python find_route.py input1.txt Start_city destination_city

              for example: python find_route input1.txt Bremen Frankfurt.

REFERENCE:

1. https://hg.python.org/cpython/file/2.7/Lib/Queue.py


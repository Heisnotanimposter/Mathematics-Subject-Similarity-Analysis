# Mathematics Subject Similarity Analysis

Project Overview
In this project, cosine similarity matrices are used to visualize the similarity between different mathematical topics. The topics covered are Linear Algebra, Differential Calculus, Integral Calculus, and Differential Equations, and their similarities are visually represented in various ways.

***Visualization Methods Used***

**Heatmap: The cosine similarity matrix is represented as a heatmap to visualize the similarity between each topic using colors.
**Network Graph: Using the cosine similarity matrix, each topic is created as a node and similarity as edges to form a network graph.
**Multidimensional Scaling (MDS): The cosine similarity matrix is converted to a distance matrix, then Multidimensional Scaling (MDS) is used to represent it in 2D space.
**Additional Visualization (Optional): Additional visualization methods can be implemented and visually represented as needed.


***Code Structure***

**ax0, ax1, ax2, ax3 classes: These classes define the code corresponding to each visualization method. Each class has a static method called plot, which is called to generate and display the respective visualization.

class ax0:
    @staticmethod
    def plot():
        # ... Heatmap visualization code ...

class ax1:
    @staticmethod
    def plot():
        # ... Network Graph visualization code ...

class ax2:
    @staticmethod
    def plot():
        # ... MDS visualization code ...

class ax3:
    @staticmethod
    def plot():
        # ... Additional visualization code (optional) ...

Main Execution Code: Calls the plot method of ax0, ax1, ax2, ax3 classes in order to generate and display each visualization.

for ax_class in [ax0, ax1, ax2, ax3]:
    ax_class.plot()
Execution Method

Install required libraries: matplotlib, seaborn, networkx, scikit-learn.
Prepare the cosine similarity matrix.
Use the main execution code above to generate and display each visualization.




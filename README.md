# Mapa Auto Organizativo (Self-Organizing Map)

The objective is to find a hidden property in the point cloud through the two-dimensional representation provided by the SOM (Self-Organizing Map). In this case, we seek to find a boundary enclosing the point cloud, which will allow us to identify how the points are grouped according to their similarity.

The solution uses the MiniSom library, which provides an implementation of the Self Organizing Map. A random point cloud is generated in the rectangle [0, 10] x [0, 10] and each point is labeled according to its position with respect to a line y = mx + b. Then, a SOM is created and trained with the training data, and the SOM is displayed along with the training points on a 2D grid. The SOM will organize the points based on their similarity in latent space and allow the boundary enclosing the point cloud to be identified.

It is important to point out that Python version 3.10.5 under Windows 10 was used to solve the problem, and the NumPy library was also enabled to generate data, manipulate matrices and perform numerical operations related to the SOM; in addition, the Matplotlib library was incorporated to better appreciate the results through graphs.

![image](https://github.com/YakoViTo/MapaAutoOrganizativo/assets/135473233/5f9eb6bf-717d-4535-8905-353af3cf3bef)

The SOM will provide a 2D visualization of the generated point cloud, where the points will be organized according to their similarity in latent space. The boundary enclosing the point cloud will be evident in the SOM, which will allow identifying how the points are grouped according to their characteristics.

The ability of the SOM to find the boundary and other structures will depend on the parameters used, the grid size, the number of training epochs, and the training data. By experimenting with different settings and data, different results and conclusions about the hidden property in the point cloud can be obtained.

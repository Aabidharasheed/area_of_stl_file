stl_file = r"C:\Users\abidhar\Downloads\myTet 9.stl"

vertices = []

file = open(stl_file, "r")

for line in file:
    line = line.strip()
    if line.startswith("vertex"):
        coordinates = line.split()
        x = float(coordinates[1])
        y = float(coordinates[2])
        z = float(coordinates[3])
        vertex = (x, y, z)
        vertices.append(vertex)
    #print(vertices)

unique_vertices = []
for coordpoint in vertices:
    if coordpoint not in unique_vertices:
        unique_vertices.append(coordpoint)
print(unique_vertices)


A = unique_vertices[0]
B = unique_vertices[1]
C = unique_vertices[2]
D = unique_vertices[3]


def triangle_area(P, Q, R):
    PQ = [Q[0] - P[0], Q[1] - P[1], Q[2] - P[2]]
    PR = [R[0] - P[0], R[1] - P[1], R[2] - P[2]]
    area = 0.5*(((PQ[1]*PR[2] - PQ[2]*PR[1])**2 + (PQ[2]*PR[0] - PQ[0]*PR[2])**2 + (PQ[0]*PR[1] - PQ[1]*PR[0])**2)**0.5)
    return area

Area1 = triangle_area(A, B, C)  # Triangle ABC
Area2 = triangle_area(A, B, D)  # Triangle ABD
Area3 = triangle_area(A, C, D)  # Triangle ACD
Area4 = triangle_area(B, C, D)  # Triangle BCD


TotalArea = Area1 + Area2 + Area3 + Area4

print("Area of Triangle ABC =", Area1)
print("Area of Triangle ABD =", Area2)
print("Area of Triangle ACD =", Area3)
print("Area of Triangle BCD =", Area4)
print("Total Surface Area of Tetrahedron =", TotalArea)

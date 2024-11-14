"""

Ray Tracing Overview
Ray Tracing is a rendering technique that simulates the way light interacts with objects in a scene to produce highly realistic images.
It’s widely used in computer graphics, 3D rendering, video games, and movies.

Ray tracing calculates the path of light as rays, simulating how they reflect, refract, and absorb upon hitting surfaces.
This technique produces visually stunning effects like shadows, reflections, and refractions, but can be computationally expensive.

Concept
Ray Generation: For each pixel on the screen, generate a ray from the camera into the scene.
Ray-Object Intersection: Check if the ray intersects any object in the scene.
Shading and Lighting: Calculate the color of the object based on lighting, reflections, and material properties.
Reflection and Refraction: If the object is reflective or transparent, cast additional rays to determine reflections and refractions.

Explanation of the Code
Ray and Sphere Classes:
The Ray class defines a ray with an origin and direction.

The Sphere class defines a sphere with a center, radius, color, and reflection property.
Ray-Sphere Intersection:
Uses the quadratic formula to determine if a ray intersects a sphere.
Lighting and Shading:
The compute_lighting function calculates the lighting at the intersection point.
Reflection:
The trace_ray function recursively traces reflected rays to simulate reflections.
Rendering the Scene:
The render_scene function generates an image by tracing rays for each pixel.

Output
When you run the code, you’ll see an image with three colored spheres rendered with lighting and reflections.

Practice
Try adding more spheres with different colors and reflection properties.
Experiment with the position of the light source to see how shadows and reflections change.
Explore adding more features like refraction, shadows, or textured surfaces.

"""

# Ray Tracing Example
# Astro Pema Software (c)
# Oba Ozai  Nov 2024

import numpy as np
import matplotlib.pyplot as plt

# Define a class for rays
class Ray:
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction / np.linalg.norm(direction)

# Define a class for spheres
class Sphere:
    def __init__(self, center, radius, color, reflection=0.5):
        self.center = center
        self.radius = radius
        self.color = color
        self.reflection = reflection

    def intersect(self, ray):
        # Calculate intersection using the quadratic formula
        oc = ray.origin - self.center
        b = 2 * np.dot(oc, ray.direction)
        c = np.dot(oc, oc) - self.radius ** 2
        discriminant = b ** 2 - 4 * c
        if discriminant < 0:
            return None
        t1 = (-b - np.sqrt(discriminant)) / 2
        t2 = (-b + np.sqrt(discriminant)) / 2
        if t1 > 0:
            return t1
        if t2 > 0:
            return t2
        return None

# Define a function for lighting
def compute_lighting(point, normal, light_position):
    light_dir = light_position - point
    light_dir = light_dir / np.linalg.norm(light_dir)
    return max(np.dot(normal, light_dir), 0)

# Ray tracing function
def trace_ray(ray, spheres, light_position, depth=3):
    closest_t = float('inf')
    closest_sphere = None
    for sphere in spheres:
        t = sphere.intersect(ray)
        if t and t < closest_t:
            closest_t = t
            closest_sphere = sphere

    if closest_sphere is None:
        return np.array([0, 0, 0])  # Background color

    # Calculate intersection point and normal
    point = ray.origin + closest_t * ray.direction
    normal = (point - closest_sphere.center) / np.linalg.norm(point - closest_sphere.center)
    
    # Calculate color with lighting
    lighting = compute_lighting(point, normal, light_position)
    color = closest_sphere.color * lighting

    # Reflection
    if depth > 0 and closest_sphere.reflection > 0:
        reflect_dir = ray.direction - 2 * np.dot(ray.direction, normal) * normal
        reflect_ray = Ray(point, reflect_dir)
        reflection_color = trace_ray(reflect_ray, spheres, light_position, depth - 1)
        color = color * (1 - closest_sphere.reflection) + reflection_color * closest_sphere.reflection

    return np.clip(color, 0, 1)

# Render the scene
def render_scene(width=400, height=300):
    camera = np.array([0, 0, -1])
    light_position = np.array([5, 5, -10])
    spheres = [
        Sphere(center=np.array([0, 0, 3]), radius=1, color=np.array([1, 0, 0]), reflection=0.5),
        Sphere(center=np.array([2, 0, 4]), radius=1, color=np.array([0, 1, 0]), reflection=0.3),
        Sphere(center=np.array([-2, 0, 4]), radius=1, color=np.array([0, 0, 1]), reflection=0.7)
    ]
    
    image = np.zeros((height, width, 3))
    for y in range(height):
        for x in range(width):
            # Convert pixel coordinate to world coordinate
            i = (x - width / 2) / width
            j = (y - height / 2) / height
            direction = np.array([i, j, 1])
            ray = Ray(camera, direction)
            color = trace_ray(ray, spheres, light_position)
            image[height - y - 1, x] = color

    return image

if __name__ == "__main__":
    print("Rendering the scene...")
    image = render_scene()
    
    # Display the rendered image
    plt.figure(figsize=(10, 7))
    plt.imshow(image)
    plt.axis('off')
    plt.show()

# EOF





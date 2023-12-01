public class ExtendedExample extends Example {

  // Inheriting the "add()" method from the parent class

  // Adding a new method specific to the ExtendedExample class
  public int multiply(int x, int y) {
    return x * y;
  }
}
public static void main(String[] args) {
  ExtendedExample extendedExample = new ExtendedExample();
  
  int sum = extendedExample.add(10, 20);         // Using the inherited "add()" method
  int product = extendedExample.multiply(5, 6);  // Using the new "multiply()" method
  
  System.out.println("Sum: " + sum);            // Prints 30
  System.out.println("Product: " + product);    // Prints 30
}
public class Vehicle {
    int wheels;
    void start() {
        System.out.println("Engine started.");
    }
}

public class Car extends Vehicle {
    int doors;
    void openDoors() {
        System.out.println("Doors are open.");
    }
}
interface Drawable {
    void draw();
}

class Circle implements Drawable {
    @Override
    public void draw() {
        // Implement how to draw a circle
    }
}

class Square implements Drawable {
    @Override
    public void draw() {
        // Implement how to draw a square
    }
}

public class Student {
    private String name;

    public void setName(String studentName) {
        name = studentName;
    }

    public String getName() {
        return name;
    }
}

public class Author {
    String name;
    // Other author-related attributes and methods
}

public class Book {
    String title;
    Author author; // Author is an object inside the Book class

    // Other book-related attributes and methods
}


// Declare an array of integers
int[] ages;

// Initialize an array with a specific size
int[] ages = new int[5];

// Assign values to array elements
ages[0] = 25;
ages[1] = 30;
// ...

// Initialize an array with values
int[] ages = {25, 30, 22, 35, 28};

// Accessing and printing values
System.out.println("First person's age: " + ages[0]);

// Using a for loop to iterate through the array
for (int i = 0; i < ages.length; i++) {
    System.out.println("Person " + i + "'s age: " + ages[i]);
}

// Getting the length of the array
int arrayLength = ages.length;

// Declaration and initialization of a 2D array
int[][] matrix = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
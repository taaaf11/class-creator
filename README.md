# class-creator

Create class using [mermaid's classDiagram](https://mermaid.js.org/syntax/classDiagram.html) like syntax.  
This program creates classes with getters and setters of mentioned attributes.

### Example

```
class Person {
  #int id
  #string name
}

class Student: Person {
  #float gpa
}
```

The above code generates the following C++ code:

```cpp
class Person {
protected:
	int id;
	string name;
public:
    int getId() {
        return id;
    }            
    void setId(int id) {
        this->id = id;
    }            
    string getName() {
        return name;
    }            
    void setName(string name) {
        this->name = name;
    }            
};
class Student: public Person {
protected:
	float gpa;
public:
    float getGpa() {
        return gpa;
    }            
    void setGpa(float gpa) {
        this->gpa = gpa;
    }            
};
```

### Usage
```
python main.py FILE_NAME -o output_file.cpp
```

where `FILE_NAME` is the file containing code for generating and the `output_file.cpp` is the file which would contain  
generated C++ code.
```

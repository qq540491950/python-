###<center>Java面试</center>
> Java 创建对象的几种方式

    (1) 用 new 语句创建对象，这是最常见的创建对象的方法。
    (2) 运用反射手段,调用 java.lang.Class 或者 java.lang.reflect.Constructor 类的 newInstance() 实例方法。
    (3) 调用对象的 clone() 方法。
    (4) 运用反序列化手段，调用 java.io.ObjectInputStream 对象的 readObject() 方法。
    注意：
        (1) 和 (2) 都会明确的显式的调用构造函数;
        (3) 是在内存上对已有对象的影印，所以不会调用构造函数;
        (4) 是从文件中还原类的对象，也不会调用构造函数。
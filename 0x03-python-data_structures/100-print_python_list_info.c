#include <Python.h>

/**
 * print_python_list_info - Prints basic information about a Python list object.
 * @p: A PyObject representing the Python list.
 */
void print_python_list_info(PyObject *p)
{
    Py_ssize_t size, allocated, i;
    PyObject *item;
    const char *type;

    size = PyList_Size(p);
    allocated = ((PyListObject *)p)->allocated;

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", allocated);

    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        type = Py_TYPE(item)->tp_name;
        printf("Element %ld: %s\n", i, type);
    }
}

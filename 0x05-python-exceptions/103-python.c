#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - Prints bytes information
 * @p: Python Object
 */
void print_python_bytes(PyObject *p)
{
	char *string;
	long int size, i, limit;

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		fflush(stdout);
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	string = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);

	if (size >= 10)
		limit = 10;
	else
		limit = size + 1;

	printf("  first %ld bytes:", limit);

	for (i = 0; i < limit; i++)
		if (string[i] >= 0)
			printf(" %02x", string[i]);
		else
			printf(" %02x", 256 + string[i]);

	printf("\n");
	fflush(stdout);
}

/**
 * print_python_float - Prints bytes information
 *
 * @p: Python Object
 * Return: no return
 */
void print_python_float(PyObject *p)
{
	double fl;

	fflush(stdout);
	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		fflush(stdout);
		return;
	}

	fl = ((PyFloatObject *)p)->ob_fval;
	printf("  value: %f\n", fl);
	fflush(stdout);
}

/**
 * print_python_list - prints some basic info about Python lists
 * @p: Python object
 */
void print_python_list(PyObject *p)
{
	long int size, i;
	PyListObject *list;

	fflush(stdout);
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		fflush(stdout);
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		obj = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
		else if (PyFloat_Check(obj))
			print_python_float(obj);
	}
	fflush(stdout);
}

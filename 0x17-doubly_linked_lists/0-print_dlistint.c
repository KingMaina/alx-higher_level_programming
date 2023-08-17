#include "lists.h"

/**
* print_dlistint - Prints the elements of a doubly linked list.
* @h: Pointer to the head of the linked list.
*
* Return: The number of elements in the list, else 0
*/
size_t print_dlistint(const dlistint_t *h)
{
	size_t count = 0;

	if (!h)
		return (0);
	if (h->prev)
	{
		while (h->prev)
			h = h->prev;
	}
	else if (!(h->next))
	{
		++count;
		printf("%d\n", h->n);
		return (count);
	}
	while (h)
	{
		++count;
		printf("%d\n", h->n);
		h = h->next;
	}

	return (count);
}

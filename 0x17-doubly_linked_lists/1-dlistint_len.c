#include "lists.h"

/**
* dlistint_len - Returns the number of elements in a doubly linked list.
* @h: Pointer to the head of the linked list.
*
* Return: The number of elements in the list, else 0
*/
size_t dlistint_len(const dlistint_t *h)
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
		return (count);
	}
	while (h)
	{
		++count;
		h = h->next;
	}

	return (count);
}

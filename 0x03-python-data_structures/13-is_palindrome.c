#include "lists.h"

int is_palindrome(listint_t **head)
{
	listint_t *curr_ptr;
	size_t list_len = 0;
	int **digits = NULL;
	int isPalindrome = 0, i, j;

	if (!head || !(*head))
		return (0);
	curr_ptr = *head;
	while (curr_ptr)
	{
		++list_len;
		curr_ptr = curr_ptr->next;
	}
	if (list_len < 0 || list_len % 2 != 0)
		return (0);
	digits = malloc(sizeof(*digits) * (list_len >> 1));
	if (!digits)
		return (0);
	curr_ptr = *head;
	for (i = 0; i < list_len >> 1; i++)
	{
		digits[i] = curr_ptr->n;
		curr_ptr = curr_ptr->next;
	}
	for (j = i - 1; curr_ptr && j >= 0; --j)
	{
		if (curr_ptr->n == digits[j])
			isPalindrome = 1;
		curr_ptr = curr_ptr->next;
	}
	if (isPalindrome == 1)
		return (1);
	return (0);
}

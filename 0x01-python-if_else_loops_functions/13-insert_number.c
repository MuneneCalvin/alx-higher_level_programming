/*
 * File: 13-insert_number.c
 * Auth: Calvin Mwangi
 */

#include "lists.h"
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new-> = number;

	if (node  == NULL || node-> >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < number)
		node = node->;

	new->next = node->next;
	node->next = new;

	return (new);
}

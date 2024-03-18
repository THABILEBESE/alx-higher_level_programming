#include <stdio.h>
#include <stdlib.h>
#include <stdio.h>
#include "lists.h"
/**
 * insert_node - insert a number into a sorted singly linked list
 * head: a pointer to a pointer to the head of the list
 * @number: integer to insert
 *
 * Return: pointer to the new node or NULL on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *new = NULL;
	listint_t *temp = NULL;

	if (!head)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (!*head || (*head)->n > number)
	{
		new->next = *head;
		return (*head = new);
	}
	else
	{
		while (current && current->n < number)
		{
			temp = current;
			current = current->next;
		}

		temp->next = new;
		new->next = current;
	}
	return (new);
}

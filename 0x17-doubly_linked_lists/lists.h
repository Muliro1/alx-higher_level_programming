#include <stdio.h>
#include <stddef.h>

#ifndef LISTS_H
#define LISTS_H

typedef struct dlistint_s
{
    int n;
    struct dlistint_s *prev;
    struct dlistint_s *next;
} dlistint_t;

size_t print_dlistint(const dlistint_t *h);
struct dlistint_s;

#endif

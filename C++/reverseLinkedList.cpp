#include <bits/stdc++.h>
using namespace std;

// # Reverse a Linked List

struct Node {
    int data;
    Node* next;
    Node(int x)
    {
        data = x;
        next = NULL;
    }
};

//  1. Iterative

struct Node* reverseList(struct Node* head)
{
    // Initialize three pointers prev as NULL, curr as head and next as NULL.
    Node* curr = head;
    Node *prev = NULL, *next = NULL;

    while (curr != NULL) {
        // Before changing next of current, store next node
        next = curr->next;
        // Now change next of current This is where actual reversing happens
        curr->next = prev;
        // Move prev and curr one step forward
        prev = curr;
        curr = next;
    }

    return prev;
}

//  2. Recursive

struct Node* reverse(struct Node* head)
{
    if (head == NULL || head->next == NULL)
        return head;

    // Divide the list in two parts - first node and rest of the linked list.
    // Call reverse for the rest of the linked list.
    Node* rest = reverse(head->next); //  Link rest to first.
    head->next->next = head; // Fix head pointer

    head->next = NULL;

    return rest;
}
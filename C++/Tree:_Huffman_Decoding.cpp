void decode_huff(node * root,string s)
{
   
   node *treeroot = root;
  // char *result = (char*)malloc(sizeof(char)*len);
    int i=0,k=0;
   while (s[i]!='\0'){
    //   printf("s[%d]%c\n", i, s[i]);
      
       if (s[i]== '1' ){
          
           root=root->right;
         //  printf("i was here");
           if (root->data != '\0'){
           //    printf("i was here");
                 printf("%c", root->data);
                 root = treeroot;
                 
                             
            }
          i++;
       }
       else {
          
           root=root->left;
            if (root->data != '\0'){
                 printf("%c", root->data);
                root = treeroot;
                 
                             
            }
          i++;
       }
       
       
       
       
       
   }
    
    
    
}



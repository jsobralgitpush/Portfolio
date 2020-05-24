#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
    // Abrimos o arquivo, e procuramos a tag do JPEG 
  
            
    
    FILE *f = fopen(argv[1], "r");
    
    if (f == NULL)
    {
        return 1;
    }
    
    unsigned char bytes[4000000];
    fread(bytes, 4000000, 1, f);
    int count[50];
    int counter = 0;
    FILE *img = fopen("000.jpg", "w");
    
    // Contadores para acabarmos com o while
    int stop_one = 0;
    int stop_two = 0;
    
    // Contadores para os nossos index;
    int j = 0;
    int k = 0;
    int l = 0;
    int m = 0;
    
    
    for (int i = 0; i < 4000000; i++)
    {
        
        // Aqui saberemos se chegamos a um JPEG
        if (bytes[i] == 0xff && bytes[i+1] == 0xd8 && bytes[i+2] == 0xff && (bytes[i+3] & 0xf0) == 0xe0) 
        {
            // Contador j para sabermos o index da próxima img usado no while abaixo
            j = i;
            
            // Aqui saberemos quantos bytes precisaremos para a nossa função fwrite
            while (stop_one == 0)
            { 
                counter++; 
                j++;
                if (bytes[j] == 0xff && bytes[j+1] == 0xd8 && bytes[j+2] == 0xff && (bytes[j+3] & 0xf0) == 0xe0)
                {
                    stop_one = 1;
                }
            }
            
            
            // Chamando uma estrutura de bytes com o tamanho da imagem JPEG achada
            unsigned char bytes_to_write[counter];
            
            
            // Counter "l" que usaremos para saber os bytes que iremos escrever em bytes_to_write
            l = i;
            m = i;
            
            // Aqui escreveremos dentro do array bytes_to_write_ os bites que correspondem a imagem
            while (stop_two == 0)
            { 
                bytes_to_write[k] = bytes[m];
                k++;
                m++;
                if (bytes[l+1] == 0xff && bytes[l+2] == 0xd8 && bytes[l+3] == 0xff && (bytes[l+4] & 0xf0) == 0xe0)
                {
                    stop_two = 1;
                }
                l++;
            }
            
            
            
            // Aqui escrevemos bytes_to_write na imagem
            fwrite(bytes_to_write, counter, 1, img);
            
            
            return 0;
            
        }

    }
    
}

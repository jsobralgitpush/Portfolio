#include "helpers.h"

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    // Soma todas as quantias de RGB, tira uma media e seta todos os pixes para esta media

    for (int i =0; i < (height); i++)
    {
        for (int j =0; j < (width); j++)
        {
            float average_color_float = ((float) (image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed)/3);
            int average_color_int = ((image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed)/3);
            {
                if ((average_color_float - average_color_int) > 0.5)
                {
                    image[i][j].rgbtBlue = average_color_int+1;
                    image[i][j].rgbtGreen = average_color_int+1;
                    image[i][j].rgbtRed = average_color_int+1;
                } else
                {
                    image[i][j].rgbtBlue = average_color_int;
                    image[i][j].rgbtGreen = average_color_int;
                    image[i][j].rgbtRed = average_color_int;
                }

            }
        }
    }

}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    // Calling array of Sepia
    float sepiaRed_float[height][width];
    float sepiaGreen_float[height][width];
    float sepiaBlue_float[height][width];

    int sepiaRed_int[height][width];
    int sepiaGreen_int[height][width];
    int sepiaBlue_int[height][width];


    // Getting the sepia collor changing ID
    for (int i =0; i < height; i++)
    {
        for (int j =0; j < width; j++)
        {
            sepiaRed_float[i][j] = .393 * image[i][j].rgbtRed + .769 * image[i][j].rgbtGreen + .189 * image[i][j].rgbtBlue;
            sepiaGreen_float[i][j] = .349 * image[i][j].rgbtRed + .686 * image[i][j].rgbtGreen + .168 * image[i][j].rgbtBlue;
            sepiaBlue_float[i][j] = .272 * image[i][j].rgbtRed + .534 * image[i][j].rgbtGreen + .131 * image[i][j].rgbtBlue;

            sepiaRed_int[i][j] = .393 * image[i][j].rgbtRed + .769 * image[i][j].rgbtGreen + .189 * image[i][j].rgbtBlue;
            sepiaGreen_int[i][j] = .349 * image[i][j].rgbtRed + .686 * image[i][j].rgbtGreen + .168 * image[i][j].rgbtBlue;
            sepiaBlue_int[i][j] = .272 * image[i][j].rgbtRed + .534 * image[i][j].rgbtGreen + .131 * image[i][j].rgbtBlue;
        }
    }


    // Transforming the image
    for (int i =0; i < height; i++)
    {
        for (int j =0; j < width; j++)
        {
            // Sepia in Red
            if (sepiaRed_float[i][j] > 255)
            {
                image[i][j].rgbtRed = 255;

            } else
            {
                if ((sepiaRed_float[i][j] - sepiaRed_int[i][j]) > 0.5)
                {
                    image[i][j].rgbtRed = sepiaRed_int[i][j] + 1;
                } else
                {

                    image[i][j].rgbtRed = sepiaRed_int[i][j];
                }
            }

            // Sepia in Green
            if (sepiaGreen_float[i][j] > 255)
            {
                image[i][j].rgbtGreen = 255;
            } else
            {
                if ((sepiaGreen_float[i][j] - sepiaGreen_int[i][j]) > 0.5)
                {
                    image[i][j].rgbtGreen = sepiaGreen_int[i][j] + 1;
                } else
                {
                    image[i][j].rgbtGreen = sepiaGreen_int[i][j];
                }
            }

            // Sepia in Blue
            if (sepiaBlue_float[i][j] > 255)
            {
                image[i][j].rgbtBlue = 255;
            }
            else
            {
                if ((sepiaBlue_float[i][j] - sepiaBlue_int[i][j]) > 0.5)
                {
                    image[i][j].rgbtBlue = sepiaBlue_int[i][j] + 1;
                } else
                {
                    image[i][j].rgbtBlue = sepiaBlue_int[i][j];
                }

            }
        }
    }

}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    int mirror_image_red[height][width];
    int mirror_image_green[height][width];
    int mirror_image_blue[height][width];


    if (width % 2 == 0)
    {
        // Pegando os pixels esquerda e jogando na direita
        for (int i = 0; i < height; i++)
        {
            for (int j = 0; j <= (width/2); j++)
            {

                mirror_image_red[i][j] = image[i][width - j - 1].rgbtRed;
                mirror_image_green[i][j] = image[i][width - j - 1].rgbtGreen; 
                mirror_image_blue[i][j] = image[i][width - j - 1].rgbtBlue;

            }
        }
        
        // Pegando os pixels da direita e jogando na esquerda
        for (int i = 0; i < height; i++)
        {
            for (int j = (width/2); j < width; j++)
            {

                mirror_image_red[i][j] = image[i][width - j - 1].rgbtRed;
                mirror_image_green[i][j] = image[i][width - j - 1].rgbtGreen; 
                mirror_image_blue[i][j] = image[i][width - j - 1].rgbtBlue;
            }
        }
        
        for (int i = 0; i < height; i++)
        {
            for (int j = 0; j < width; j++)
            {
                image[i][j].rgbtRed = mirror_image_red[i][j];
                image[i][j].rgbtGreen = mirror_image_green[i][j]; 
                image[i][j].rgbtBlue = mirror_image_blue[i][j];
            }
        }

    } else
    {
        // Pegando os pixels esquerda e jogando na direita
        for (int i = 0; i < height; i++)
        {
            for (int j = 0; j <= ((width/2)-0.5); j++)
            {

                mirror_image_red[i][j] = image[i][width - j - 1].rgbtRed;
                mirror_image_green[i][j] = image[i][width - j - 1].rgbtGreen; 
                mirror_image_blue[i][j] = image[i][width - j - 1].rgbtBlue;

            }
        }
        
        // Pegando os pixels da direita e jogando na esquerda
        for (int i = 0; i < height; i++)
        {
            for (int j = ((width/2)+0.5); j < width; j++)
            {

                mirror_image_red[i][j] = image[i][width - j - 1].rgbtRed;
                mirror_image_green[i][j] = image[i][width - j - 1].rgbtGreen; 
                mirror_image_blue[i][j] = image[i][width - j - 1].rgbtBlue;
            }
        }
        
        for (int i = 0; i < height; i++)
        {
            for (int j = 0; j < width; j++)
            {
                image[i][j].rgbtRed = mirror_image_red[i][j];
                image[i][j].rgbtGreen = mirror_image_green[i][j]; 
                image[i][j].rgbtBlue = mirror_image_blue[i][j];
            }
        }
    }
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // Voce pega a media de todos ao redor

    // Counters
    int blur_image_red[height][width];
    int blur_image_green[height][width];
    int blur_image_blue[height][width];

    int pixel_left_red;
    int pixel_left_green;
    int pixel_left_blue;

    int pixel_right_red;
    int pixel_right_green;
    int pixel_right_blue;

    int pixel_top_red;
    int pixel_top_green;
    int pixel_top_blue;

    int pixel_bottom_red;
    int pixel_bottom_green;
    int pixel_bottom_blue;

    int pixel_left_top_corner_red;
    int pixel_left_top_corner_green;
    int pixel_left_top_corner_blue;

    int pixel_right_top_corner_red;
    int pixel_right_top_corner_green;
    int pixel_right_top_corner_blue;

    int pixel_left_bottom_corner_red;
    int pixel_left_bottom_corner_green;
    int pixel_left_bottom_corner_blue;

    int pixel_right_bottom_corner_red;
    int pixel_right_bottom_corner_green;
    int pixel_right_bottom_corner_blue;

    int sum_red;
    int sum_green;
    int sum_blue;

    float average_red_float;
    float average_green_float;
    float average_blue_float;
    
    int average_red_int;
    int average_green_int;
    int average_blue_int;


    // Vai ser uma lógica para os pixels do centro e outra para os pixels da bord
    // Sera que faz alguma diferença somar todas as cores e depois fazer a media



    for (int i = 0; i <= (height-1); i++)
    {
        for (int j = 0; j <= (width-1); j++)
        {
            // Pixels do centro

            if ( i > 0 && j > 0 && i < (height-1) && j < (width-1))
            {
    // Calculating the RGB of each pixel from the neighborhood

                // Left pixel (i - 1 ; same j)
                pixel_left_red = image[i - 1][j].rgbtRed;
                pixel_left_green = image[i - 1][j].rgbtGreen;
                pixel_left_blue = image[i - 1][j].rgbtBlue;


                // Right pixel (i + 1; same j)
                pixel_right_red = image[i + 1][j].rgbtRed;
                pixel_right_green = image[i + 1][j].rgbtGreen;
                pixel_right_blue = image[i + 1][j].rgbtBlue;


                // Top pixel (same i; j - 1)
                pixel_top_red = image[i][j - 1].rgbtRed;
                pixel_top_green = image[i][j - 1].rgbtGreen;
                pixel_top_blue = image[i][j - 1].rgbtBlue;


                // Bottom pixel (same i; j + 1)
                pixel_bottom_red = image[i][j + 1].rgbtRed;
                pixel_bottom_green = image[i][j + 1].rgbtGreen;
                pixel_bottom_blue = image[i][j + 1].rgbtBlue;


                // Left top corner (i-1; j - 1)
                pixel_left_top_corner_red = image[i - 1][j - 1].rgbtRed;
                pixel_left_top_corner_green = image[i - 1][j - 1].rgbtGreen;
                pixel_left_top_corner_blue = image[i - 1][j - 1].rgbtBlue;


                // Right Top corner (i+1; j - 1)
                pixel_right_top_corner_red = image[i + 1][j - 1].rgbtRed;
                pixel_right_top_corner_green = image[i + 1][j - 1].rgbtGreen;
                pixel_right_top_corner_blue = image[i + 1][j - 1].rgbtBlue;


                // Left bottom corner (i - 1; j + 1)
                pixel_left_bottom_corner_red = image[i - 1][j + 1].rgbtRed;
                pixel_left_bottom_corner_green = image[i - 1][j + 1].rgbtGreen;
                pixel_left_bottom_corner_blue = image[i - 1][j + 1].rgbtBlue;


                // Right bottom corner (i + 1; j + 1)
                pixel_right_bottom_corner_red = image[i + 1][j + 1].rgbtRed;
                pixel_right_bottom_corner_green = image[i + 1][j + 1].rgbtGreen;
                pixel_right_bottom_corner_blue = image[i + 1][j + 1].rgbtBlue;




        // Calculate the average of each one

                // sum
                sum_red = pixel_left_red + pixel_right_red + pixel_top_red + pixel_bottom_red + pixel_left_top_corner_red + pixel_right_top_corner_red + pixel_left_bottom_corner_red + pixel_right_bottom_corner_red;
                sum_green = pixel_left_green + pixel_right_green + pixel_top_green + pixel_bottom_green + pixel_left_top_corner_green + pixel_right_top_corner_green + pixel_left_bottom_corner_green + pixel_right_bottom_corner_green;
                sum_blue = pixel_left_blue + pixel_right_blue + pixel_top_blue + pixel_bottom_blue + pixel_left_top_corner_blue + pixel_right_top_corner_blue + pixel_left_bottom_corner_blue + pixel_right_bottom_corner_blue;

                // Average float
                average_red_float = ((float)(image[i][j].rgbtRed + sum_red))/9;
                average_green_float = ((float)(image[i][j].rgbtGreen + sum_green))/9;
                average_blue_float = ((float)(image[i][j].rgbtBlue + sum_blue))/9;
                
                // Average int
                average_red_int = (image[i][j].rgbtRed + sum_red)/9;
                average_green_int = (image[i][j].rgbtGreen + sum_green)/9;
                average_blue_int = (image[i][j].rgbtBlue + sum_blue)/9;

                // Filling blur_image_red
                if (average_red_float - average_red_int > 0.5) 
                {
                    blur_image_red[i][j] =  average_red_int + 1;
                } else
                {
                    blur_image_red[i][j] =  average_red_int;
                }
                
                // Filling blur_image_green
                if (average_green_float - average_green_int > 0.5) 
                {
                    blur_image_green[i][j] =  average_green_int + 1;
                } else
                {
                    blur_image_green[i][j] =  average_green_int;
                }
                
                // Filling blur_image_blue
                if (average_blue_float - average_blue_int > 0.5) 
                {
                    blur_image_blue[i][j] =  average_blue_int + 1;
                } else
                {
                    blur_image_blue[i][j] =  average_blue_int;
                }
                
            
                
            // Left top corner

            } else if (i == 0 && j == 0)
            {

                // Right pixel (i + 1; same j)
                pixel_right_red = image[i + 1][j].rgbtRed;
                pixel_right_green = image[i + 1][j].rgbtGreen;
                pixel_right_blue = image[i + 1][j].rgbtBlue;


                // Bottom pixel (same i; j + 1)
                pixel_bottom_red = image[i][j + 1].rgbtRed;
                pixel_bottom_green = image[i][j + 1].rgbtGreen;
                pixel_bottom_blue = image[i][j + 1].rgbtBlue;


                // Right bottom corner (i + 1; j + 1)
                pixel_right_bottom_corner_red = image[i + 1][j + 1].rgbtRed;
                pixel_right_bottom_corner_green = image[i + 1][j + 1].rgbtGreen;
                pixel_right_bottom_corner_blue = image[i + 1][j + 1].rgbtBlue;



        // Calculate the average of each one

                // sum
                sum_red = pixel_right_red + pixel_bottom_red + pixel_right_bottom_corner_red;
                sum_green =  pixel_right_green + pixel_bottom_green + pixel_right_bottom_corner_green;
                sum_blue = pixel_right_blue + pixel_bottom_blue + pixel_right_bottom_corner_blue;

                // Average float
                average_red_float = ((float)(image[i][j].rgbtRed + sum_red))/4;
                average_green_float = ((float)(image[i][j].rgbtGreen + sum_green))/4;
                average_blue_float = ((float)(image[i][j].rgbtBlue + sum_blue))/4;
                
                // Average int
                average_red_int = (image[i][j].rgbtRed + sum_red)/4;
                average_green_int = (image[i][j].rgbtGreen + sum_green)/4;
                average_blue_int = (image[i][j].rgbtBlue + sum_blue)/4;

                // Filling blur_image_red
                if (average_red_float - average_red_int > 0.5) 
                {
                    blur_image_red[i][j] =  average_red_int + 1;
                } else
                {
                    blur_image_red[i][j] =  average_red_int;
                }
                
                // Filling blur_image_green
                if (average_green_float - average_green_int > 0.5) 
                {
                    blur_image_green[i][j] =  average_green_int + 1;
                } else
                {
                    blur_image_green[i][j] =  average_green_int;
                }
                
                // Filling blur_image_blue
                if (average_blue_float - average_blue_int > 0.5) 
                {
                    blur_image_blue[i][j] =  average_blue_int + 1;
                } else
                {
                    blur_image_blue[i][j] =  average_blue_int;
                }
                
            // Right top corner

            } else if (i == (height-1) && j == 0)
            {
                // Left pixel (i - 1; same j)
                pixel_left_red = image[i - 1][j].rgbtRed;
                pixel_left_green = image[i - 1][j].rgbtGreen;
                pixel_left_blue = image[i - 1][j].rgbtBlue;

                // Bottom pixel (same i; j + 1)
                pixel_bottom_red = image[i][j + 1].rgbtRed;
                pixel_bottom_green = image[i][j + 1].rgbtGreen;
                pixel_bottom_blue = image[i][j + 1].rgbtBlue;

                // Left bottom corner (i - 1; j + 1)
                pixel_left_bottom_corner_red = image[i - 1][j + 1].rgbtRed;
                pixel_left_bottom_corner_green = image[i - 1][j + 1].rgbtGreen;
                pixel_left_bottom_corner_blue = image[i - 1][j + 1].rgbtBlue;


        // Calculate the average of each one

                // sum
                sum_red = pixel_left_red + pixel_bottom_red + pixel_left_bottom_corner_red;
                sum_green = pixel_left_green + pixel_bottom_green + pixel_left_bottom_corner_green;
                sum_blue = pixel_left_blue + pixel_bottom_blue + pixel_left_bottom_corner_blue;

                // Average float
                average_red_float = ((float)(image[i][j].rgbtRed + sum_red))/4;
                average_green_float = ((float)(image[i][j].rgbtGreen + sum_green))/4;
                average_blue_float = ((float)(image[i][j].rgbtBlue + sum_blue))/4;
                
                // Average int
                average_red_int = (image[i][j].rgbtRed + sum_red)/4;
                average_green_int = (image[i][j].rgbtGreen + sum_green)/4;
                average_blue_int = (image[i][j].rgbtBlue + sum_blue)/4;

                // Filling blur_image_red
                if (average_red_float - average_red_int > 0.5) 
                {
                    blur_image_red[i][j] =  average_red_int + 1;
                } else
                {
                    blur_image_red[i][j] =  average_red_int;
                }
                
                // Filling blur_image_green
                if (average_green_float - average_green_int > 0.5) 
                {
                    blur_image_green[i][j] =  average_green_int + 1;
                } else
                {
                    blur_image_green[i][j] =  average_green_int;
                }
                
                // Filling blur_image_blue
                if (average_blue_float - average_blue_int > 0.5) 
                {
                    blur_image_blue[i][j] =  average_blue_int + 1;
                } else
                {
                    blur_image_blue[i][j] =  average_blue_int;
                }

            } else if (i == 0 && j == (width-1))
            {
                // Right pixel (i + 1; same j)
                pixel_right_red = image[i + 1][j].rgbtRed;
                pixel_right_green = image[i + 1][j].rgbtGreen;
                pixel_right_blue = image[i + 1][j].rgbtBlue;

                // Top pixel (same i; j - 1)
                pixel_top_red = image[i][j - 1].rgbtRed;
                pixel_top_green = image[i][j - 1].rgbtGreen;
                pixel_top_blue = image[i][j - 1].rgbtBlue;

                // Right Top corner (i+1; j - 1)
                pixel_right_top_corner_red = image[i + 1][j - 1].rgbtRed;
                pixel_right_top_corner_green = image[i + 1][j - 1].rgbtGreen;
                pixel_right_top_corner_blue = image[i + 1][j - 1].rgbtBlue;


        // Calculate the average of each one

                // sum
                sum_red = pixel_right_red + pixel_top_red + pixel_right_top_corner_red;
                sum_green = pixel_right_green + pixel_top_green + pixel_right_top_corner_green;
                sum_blue = pixel_right_blue + pixel_top_blue + pixel_right_top_corner_blue;

                 // Average float
                average_red_float = ((float)(image[i][j].rgbtRed + sum_red))/4;
                average_green_float = ((float)(image[i][j].rgbtGreen + sum_green))/4;
                average_blue_float = ((float)(image[i][j].rgbtBlue + sum_blue))/4;
                
                // Average int
                average_red_int = (image[i][j].rgbtRed + sum_red)/4;
                average_green_int = (image[i][j].rgbtGreen + sum_green)/4;
                average_blue_int = (image[i][j].rgbtBlue + sum_blue)/4;

                // Filling blur_image_red
                if (average_red_float - average_red_int > 0.5) 
                {
                    blur_image_red[i][j] =  average_red_int + 1;
                } else
                {
                    blur_image_red[i][j] =  average_red_int;
                }
                
                // Filling blur_image_green
                if (average_green_float - average_green_int > 0.5) 
                {
                    blur_image_green[i][j] =  average_green_int + 1;
                } else
                {
                    blur_image_green[i][j] =  average_green_int;
                }
                
                // Filling blur_image_blue
                if (average_blue_float - average_blue_int > 0.5) 
                {
                    blur_image_blue[i][j] =  average_blue_int + 1;
                } else
                {
                    blur_image_blue[i][j] =  average_blue_int;
                }
                
            } else if ( i == (height-1) && j == (width-1))
            {
                 // Left pixel (i - 1 ; same j)
                pixel_left_red = image[i - 1][j].rgbtRed;
                pixel_left_green = image[i - 1][j].rgbtGreen;
                pixel_left_blue = image[i - 1][j].rgbtBlue;

                // Top pixel (same i; j - 1)
                pixel_top_red = image[i][j - 1].rgbtRed;
                pixel_top_green = image[i][j - 1].rgbtGreen;
                pixel_top_blue = image[i][j - 1].rgbtBlue;

                // Left top corner (i-1; j - 1)
                pixel_left_top_corner_red = image[i - 1][j - 1].rgbtRed;
                pixel_left_top_corner_green = image[i - 1][j - 1].rgbtGreen;
                pixel_left_top_corner_blue = image[i - 1][j - 1].rgbtBlue;


        // Calculate the average of each one

                // sum
                sum_red = pixel_left_red + pixel_top_red + pixel_left_top_corner_red;
                sum_green = pixel_left_green + pixel_top_green + pixel_left_top_corner_green;
                sum_blue = pixel_left_blue + pixel_top_blue + pixel_left_top_corner_blue;

                 // Average float
                average_red_float = ((float)(image[i][j].rgbtRed + sum_red))/4;
                average_green_float = ((float)(image[i][j].rgbtGreen + sum_green))/4;
                average_blue_float = ((float)(image[i][j].rgbtBlue + sum_blue))/4;
                
                // Average int
                average_red_int = (image[i][j].rgbtRed + sum_red)/4;
                average_green_int = (image[i][j].rgbtGreen + sum_green)/4;
                average_blue_int = (image[i][j].rgbtBlue + sum_blue)/4;

                // Filling blur_image_red
                if (average_red_float - average_red_int > 0.5) 
                {
                    blur_image_red[i][j] =  average_red_int + 1;
                } else
                {
                    blur_image_red[i][j] =  average_red_int;
                }
                
                // Filling blur_image_green
                if (average_green_float - average_green_int > 0.5) 
                {
                    blur_image_green[i][j] =  average_green_int + 1;
                } else
                {
                    blur_image_green[i][j] =  average_green_int;
                }
                
                // Filling blur_image_blue
                if (average_blue_float - average_blue_int > 0.5) 
                {
                    blur_image_blue[i][j] =  average_blue_int + 1;
                } else
                {
                    blur_image_blue[i][j] =  average_blue_int;
                }
                
            // Left side

            } else if (i == 0 && j > 0 && j < (width-1))
            {
                // Right pixel (i + 1; same j)
                pixel_right_red = image[i + 1][j].rgbtRed;
                pixel_right_green = image[i + 1][j].rgbtGreen;
                pixel_right_blue = image[i + 1][j].rgbtBlue;

                // Top pixel (same i; j - 1)
                pixel_top_red = image[i][j - 1].rgbtRed;
                pixel_top_green = image[i][j - 1].rgbtGreen;
                pixel_top_blue = image[i][j - 1].rgbtBlue;

                // Bottom pixel (same i; j + 1)
                pixel_bottom_red = image[i][j + 1].rgbtRed;
                pixel_bottom_green = image[i][j + 1].rgbtGreen;
                pixel_bottom_blue = image[i][j + 1].rgbtBlue;

                // Right Top corner (i+1; j - 1)
                pixel_right_top_corner_red = image[i + 1][j - 1].rgbtRed;
                pixel_right_top_corner_green = image[i + 1][j - 1].rgbtGreen;
                pixel_right_top_corner_blue = image[i + 1][j - 1].rgbtBlue;

                // Right bottom corner (i + 1; j + 1)
                pixel_right_bottom_corner_red = image[i + 1][j + 1].rgbtRed;
                pixel_right_bottom_corner_green = image[i + 1][j + 1].rgbtGreen;
                pixel_right_bottom_corner_blue = image[i + 1][j + 1].rgbtBlue;


        // Calculate the average of each one

                // sum
                sum_red =  pixel_right_red + pixel_top_red + pixel_bottom_red + pixel_right_top_corner_red + pixel_right_bottom_corner_red;
                sum_green =  pixel_right_green + pixel_top_green + pixel_bottom_green + pixel_right_top_corner_green + pixel_right_bottom_corner_green;
                sum_blue = pixel_right_blue + pixel_top_blue + pixel_bottom_blue  + pixel_right_top_corner_blue  + pixel_right_bottom_corner_blue;

                // Average float
                average_red_float = ((float)(image[i][j].rgbtRed + sum_red))/6;
                average_green_float = ((float)(image[i][j].rgbtGreen + sum_green))/6;
                average_blue_float = ((float)(image[i][j].rgbtBlue + sum_blue))/6;
                
                // Average int
                average_red_int = (image[i][j].rgbtRed + sum_red)/6;
                average_green_int = (image[i][j].rgbtGreen + sum_green)/6;
                average_blue_int = (image[i][j].rgbtBlue + sum_blue)/6;

                // Filling blur_image_red
                if (average_red_float - average_red_int > 0.5) 
                {
                    blur_image_red[i][j] =  average_red_int + 1;
                } else
                {
                    blur_image_red[i][j] =  average_red_int;
                }
                
                // Filling blur_image_green
                if (average_green_float - average_green_int > 0.5) 
                {
                    blur_image_green[i][j] =  average_green_int + 1;
                } else
                {
                    blur_image_green[i][j] =  average_green_int;
                }
                
                // Filling blur_image_blue
                if (average_blue_float - average_blue_int > 0.5) 
                {
                    blur_image_blue[i][j] =  average_blue_int + 1;
                } else
                {
                    blur_image_blue[i][j] =  average_blue_int;
                }
                
            // Right side

            } else if (i == (height-1) && j > 0 && j < (width-1))
            {
                // Left pixel (i - 1 ; same j)
                pixel_left_red = image[i - 1][j].rgbtRed;
                pixel_left_green = image[i - 1][j].rgbtGreen;
                pixel_left_blue = image[i - 1][j].rgbtBlue;

                // Top pixel (same i; j - 1)
                pixel_top_red = image[i][j - 1].rgbtRed;
                pixel_top_green = image[i][j - 1].rgbtGreen;
                pixel_top_blue = image[i][j - 1].rgbtBlue;

                // Bottom pixel (same i; j + 1)
                pixel_bottom_red = image[i][j + 1].rgbtRed;
                pixel_bottom_green = image[i][j + 1].rgbtGreen;
                pixel_bottom_blue = image[i][j + 1].rgbtBlue;

                // Left top corner (i-1; j - 1)
                pixel_left_top_corner_red = image[i - 1][j - 1].rgbtRed;
                pixel_left_top_corner_green = image[i - 1][j - 1].rgbtGreen;
                pixel_left_top_corner_blue = image[i - 1][j - 1].rgbtBlue;

                // Left bottom corner (i - 1; j + 1)
                pixel_left_bottom_corner_red = image[i - 1][j + 1].rgbtRed;
                pixel_left_bottom_corner_green = image[i - 1][j + 1].rgbtGreen;
                pixel_left_bottom_corner_blue = image[i - 1][j + 1].rgbtBlue;




        // Calculate the average of each one

                // sum
                sum_red = pixel_left_red + pixel_top_red + pixel_bottom_red + pixel_left_top_corner_red + pixel_left_bottom_corner_red;
                sum_green = pixel_left_green + pixel_top_green + pixel_bottom_green + pixel_left_top_corner_green + pixel_left_bottom_corner_green;
                sum_blue = pixel_left_blue + pixel_top_blue + pixel_bottom_blue + pixel_left_top_corner_blue + pixel_left_bottom_corner_blue;

                 // Average float
                average_red_float = ((float)(image[i][j].rgbtRed + sum_red))/6;
                average_green_float = ((float)(image[i][j].rgbtGreen + sum_green))/6;
                average_blue_float = ((float)(image[i][j].rgbtBlue + sum_blue))/6;
                
                // Average int
                average_red_int = (image[i][j].rgbtRed + sum_red)/6;
                average_green_int = (image[i][j].rgbtGreen + sum_green)/6;
                average_blue_int = (image[i][j].rgbtBlue + sum_blue)/6;

                // Filling blur_image_red
                if (average_red_float - average_red_int > 0.5) 
                {
                    blur_image_red[i][j] =  average_red_int + 1;
                } else
                {
                    blur_image_red[i][j] =  average_red_int;
                }
                
                // Filling blur_image_green
                if (average_green_float - average_green_int > 0.5) 
                {
                    blur_image_green[i][j] =  average_green_int + 1;
                } else
                {
                    blur_image_green[i][j] =  average_green_int;
                }
                
                // Filling blur_image_blue
                if (average_blue_float - average_blue_int > 0.5) 
                {
                    blur_image_blue[i][j] =  average_blue_int + 1;
                } else
                {
                    blur_image_blue[i][j] =  average_blue_int;
                }
                
            // Top side

            } else if (j == 0 && i > 0 && i < (height-1))
            {
                // Left pixel (i - 1 ; same j)
                pixel_left_red = image[i - 1][j].rgbtRed;
                pixel_left_green = image[i - 1][j].rgbtGreen;
                pixel_left_blue = image[i - 1][j].rgbtBlue;

                // Right pixel (i + 1; same j)
                pixel_right_red = image[i + 1][j].rgbtRed;
                pixel_right_green = image[i + 1][j].rgbtGreen;
                pixel_right_blue = image[i + 1][j].rgbtBlue;

                // Bottom pixel (same i; j + 1)
                pixel_bottom_red = image[i][j + 1].rgbtRed;
                pixel_bottom_green = image[i][j + 1].rgbtGreen;
                pixel_bottom_blue = image[i][j + 1].rgbtBlue;

                // Left bottom corner (i - 1; j + 1)
                pixel_left_bottom_corner_red = image[i - 1][j + 1].rgbtRed;
                pixel_left_bottom_corner_green = image[i - 1][j + 1].rgbtGreen;
                pixel_left_bottom_corner_blue = image[i - 1][j + 1].rgbtBlue;

                // Right bottom corner (i + 1; j + 1)
                pixel_right_bottom_corner_red = image[i + 1][j + 1].rgbtRed;
                pixel_right_bottom_corner_green = image[i + 1][j + 1].rgbtGreen;
                pixel_right_bottom_corner_blue = image[i + 1][j + 1].rgbtBlue;




        // Calculate the average of each one

                // sum
                sum_red = pixel_left_red + pixel_right_red + pixel_bottom_red + pixel_left_bottom_corner_red + pixel_right_bottom_corner_red;
                sum_green = pixel_left_green + pixel_right_green + pixel_bottom_green + pixel_left_bottom_corner_green + pixel_right_bottom_corner_green;
                sum_blue = pixel_left_blue + pixel_right_blue + pixel_bottom_blue + pixel_left_bottom_corner_blue + pixel_right_bottom_corner_blue;

                 // Average float
                average_red_float = ((float)(image[i][j].rgbtRed + sum_red))/6;
                average_green_float = ((float)(image[i][j].rgbtGreen + sum_green))/6;
                average_blue_float = ((float)(image[i][j].rgbtBlue + sum_blue))/6;
                
                // Average int
                average_red_int = (image[i][j].rgbtRed + sum_red)/6;
                average_green_int = (image[i][j].rgbtGreen + sum_green)/6;
                average_blue_int = (image[i][j].rgbtBlue + sum_blue)/6;

                // Filling blur_image_red
                if (average_red_float - average_red_int > 0.5) 
                {
                    blur_image_red[i][j] =  average_red_int + 1;
                } else
                {
                    blur_image_red[i][j] =  average_red_int;
                }
                
                // Filling blur_image_green
                if (average_green_float - average_green_int > 0.5) 
                {
                    blur_image_green[i][j] =  average_green_int + 1;
                } else
                {
                    blur_image_green[i][j] =  average_green_int;
                }
                
                // Filling blur_image_blue
                if (average_blue_float - average_blue_int > 0.5) 
                {
                    blur_image_blue[i][j] =  average_blue_int + 1;
                } else
                {
                    blur_image_blue[i][j] =  average_blue_int;
                }
                
            // Down side

            } else if (j == (width-1) && i > 0 && i < (height-1))
            {
                 // Left pixel (i - 1 ; same j)
                pixel_left_red = image[i - 1][j].rgbtRed;
                pixel_left_green = image[i - 1][j].rgbtGreen;
                pixel_left_blue = image[i - 1][j].rgbtBlue;


                // Right pixel (i + 1; same j)
                pixel_right_red = image[i + 1][j].rgbtRed;
                pixel_right_green = image[i + 1][j].rgbtGreen;
                pixel_right_blue = image[i + 1][j].rgbtBlue;


                // Top pixel (same i; j - 1)
                pixel_top_red = image[i][j - 1].rgbtRed;
                pixel_top_green = image[i][j - 1].rgbtGreen;
                pixel_top_blue = image[i][j - 1].rgbtBlue;


                // Left top corner (i-1; j - 1)
                pixel_left_top_corner_red = image[i - 1][j - 1].rgbtRed;
                pixel_left_top_corner_green = image[i - 1][j - 1].rgbtGreen;
                pixel_left_top_corner_blue = image[i - 1][j - 1].rgbtBlue;


                // Right Top corner (i+1; j - 1)
                pixel_right_top_corner_red = image[i + 1][j - 1].rgbtRed;
                pixel_right_top_corner_green = image[i + 1][j - 1].rgbtGreen;
                pixel_right_top_corner_blue = image[i + 1][j - 1].rgbtBlue;


        // Calculate the average of each one

                // sum
                sum_red = pixel_left_red + pixel_right_red + pixel_top_red + pixel_left_top_corner_red + pixel_right_top_corner_red;
                sum_green = pixel_left_green + pixel_right_green + pixel_top_green + pixel_left_top_corner_green + pixel_right_top_corner_green;
                sum_blue = pixel_left_blue + pixel_right_blue + pixel_top_blue + pixel_left_top_corner_blue + pixel_right_top_corner_blue;

                // Average float
                average_red_float = ((float)(image[i][j].rgbtRed + sum_red))/6;
                average_green_float = ((float)(image[i][j].rgbtGreen + sum_green))/6;
                average_blue_float = ((float)(image[i][j].rgbtBlue + sum_blue))/6;
                
                // Average int
                average_red_int = (image[i][j].rgbtRed + sum_red)/6;
                average_green_int = (image[i][j].rgbtGreen + sum_green)/6;
                average_blue_int = (image[i][j].rgbtBlue + sum_blue)/6;

                // Filling blur_image_red
                if (average_red_float - average_red_int > 0.5) 
                {
                    blur_image_red[i][j] =  average_red_int + 1;
                } else
                {
                    blur_image_red[i][j] =  average_red_int;
                }
                
                // Filling blur_image_green
                if (average_green_float - average_green_int > 0.5) 
                {
                    blur_image_green[i][j] =  average_green_int + 1;
                } else
                {
                    blur_image_green[i][j] =  average_green_int;
                }
                
                // Filling blur_image_blue
                if (average_blue_float - average_blue_int > 0.5) 
                {
                    blur_image_blue[i][j] =  average_blue_int + 1;
                } else
                {
                    blur_image_blue[i][j] =  average_blue_int;
                }
                
            }

        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j].rgbtRed = blur_image_red[i][j];
            image[i][j].rgbtGreen = blur_image_green[i][j]; 
            image[i][j].rgbtBlue = blur_image_blue[i][j];
        }
    }

}

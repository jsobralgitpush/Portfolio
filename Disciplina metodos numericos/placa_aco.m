function placaresfriada=deltax,deltay,deltat
  #para um primeiro teste, vamos colocar aqui o deltax, deltay e deltat
  deltax=0.24;
  deltay=0.1;
  deltat=10;
  
  #constantes que estamos usando 
  hagua = (3.6/60)*10^6;
  har = 9;
  k_aco = (1.8/60)*10^5;
  densidade_aco = 7872;
  calor_esp_aco = 486;
  tamanho_x_placa = 2.4;
  tamanho_y_placa = 1;
  tamanho_z_placa = 0.1;
  area_placa = tamanho_x_placa*tamanho_y_placa;
  alfa = densidade_aco*calor_esp_aco/k_aco;
  gama2 = deltat/(alfa);
  
  C1 = 1 + 2*(gama2)/(deltax^2) + 2*(gama2)/(deltay^2);
  C2 = -gama2/deltax^2;
  C3 = -gama2/deltax^2;
  C4 = -gama2/deltay^2;
  C5 = -gama2/deltay^2;
  
  #para testar, vamos chutar um tempo final
  tempo_final = 120;
  
  
  #divisao dos intervalos que usaremos
  nx=tamanho_x_placa/deltax;
  ny=tamanho_y_placa/deltay;
  nt=tempo_final/deltat;
  
  
  #chamando a matriz de zeros (2D e 1D)
  
  #condicoes de contorno
  Tinicial = 1050+273;
  Tfinal = 25+273;
  T(:,:,1) = Tinicial;
  T1(:,1)= Tinicial;


  T=zeros(nx,ny,nt);
  T1=zeros(nx,nt);
  T2=zeros(nx,ny,nt);
  W=zeros(nx+2,ny+2,nt);
  W_reso=zeros(nx+2,1,nt);
  W1 = zeros(nx,ny,nt);
 
  
  
  #funcoes que estamos usando (2 dimensoes)  
    #derivada_segunda_y = (T(i,j+1,k) - 2*T(i,j,k) + T(i,j+1,k))/(deltay^2)
    #derivada_segunda_x = (T(i+1,j,k) - 2*T(i,j,k) + T(i-1,j,k))/(deltax^2)
    #derivada_primeira_y = (T(i,j+1,k) - T(i,j-1,k))/(2*deltay)
    #derivada_primeira_x = (T(i+1,j,k) - T(i-1,j,k))/(2*deltax)
    #derivada_primeira_tempo = (T(i,j,k+1)  - T(i,j,k))/(2*deltat)
    
   #funcao que estamos usando (1 dimensao)
    #derivada_segunda_x = (T(i+1,k) - 2*T(i,k) + T(i-1,k))/(deltax^2)
    #derivada_primeira_tempo = (T(i,k+1)  - T(i,k))/(2*deltat)
  
#tentando resolver um sistema nas condicoes de contorno
for k=2:nt  
  for j=1:ny+2
    for i=1:nx+2
      if i==1 && j==1
        W(i,j,k) = C1 + (gama2/deltax)*(hagua/k_aco)*2+(gama2/deltay)*(hagua/k_aco)*2;
        W(i+1,j,k) =2*C2;
        W(i,j+1,k) =2*C4;
        #W_reso(i,1,k) = W(i,j,k-1) +(gama2/deltax)*2*hagua*Tfinal/k_aco+(gama2/deltay)*2*hagua*Tfinal/k_aco;
      elseif i==1 && j<ny+2 && j!=1
        W(i,j,k) = C1 + (gama2/deltax)*(hagua/k_aco)*2;
        W(i+1,j,k) =2*C2;
        W(i,j+1,k) = C4;
        W(i,j-1,k) = C5;
        W_reso(i,1,k) = W(i,j,k-1) +(gama2/deltax)*2*hagua*Tfinal/k_aco;
      elseif i==1 && j==ny+2
        W(i,j,k) = 2*C1 - (gama2/deltay)*(hagua/k_aco)*2 + (gama2/deltax)*(hagua/k_aco)*2;
        W(i+1,j,k) = 2*C3;
        W(i,j-1,k) = 2*C4;
      elseif j==1 && i<nx+2 && i!=1
        W(i,j,k) = C1 +(gama2/deltay)*(hagua/k_aco)*2;
        W(i,j+1,k) =2*C4;
        W(i+1,j,k) = C2;
        W(i-1,j,k) = C3;
        W_reso(i,1,k) = W(i,j,k-1) -(gama2/deltay)*2*hagua*Tfinal/k_aco;
      elseif i==nx+2 && j<ny+2 && j>1 
        W(i,j,k) = C1 - (gama2/deltax)*(hagua/k_aco)*2;
        W(i-1,j,k) =2*C2;
        W(i,j+1,k) = C4;
        W(i,j-1,k) = C5;
        W_reso(i,1,k) = W(i,j,k-1) -(gama2/deltax)*2*hagua*Tfinal/k_aco;
      elseif j==ny+2 && i<nx+2 && i!=1
        W(i,j,k) = C1 - (gama2/deltay)*(hagua/k_aco)*2;
        W(i,j-1,k)=2*C5;
        W(i+1,j,k) = C2;
        W(i-1,j,k) = C3;
        W_reso(i,1,k) = W(i,j,k-1) -(gama2/deltay)*2*hagua*Tfinal/k_aco;
      elseif j==1 && i==nx+2
        W(i,j,k) = 2*C1 + (gama2/deltay)*(hagua/k_aco)*2 - (gama2/deltax)*(hagua/k_aco)*2;
        W(i-1,j,k) = 2*C3;
        W(i,j+1,k) = 2*C4;
      elseif i==(nx+2) && j==(ny+2)
        W(i,j,k) = C1 - (gama2/deltax)*(hagua/k_aco)*2 -(gama2/deltay)*(hagua/k_aco)*2;
        W(i-1,j,k) =2*C2;
        W(i,j-1,k)=2*C5;
        W_reso(i,1,k) = W(i,j,k-1) -(gama2/deltax)*2*hagua*Tfinal/k_aco-(gama2/deltay)*2*hagua*Tfinal/k_aco;
      else
        W(i,j,k) = C1;
        W(i+1,j,k) = C2;
        W(i-1,j,k) = C3;
        W(i,j+1,k) = C4;
        W(i,j-1,k) = C5;
        W_reso(i,1,k) = W(i,j,k-1);
      endif
    endfor
  endfor     
endfor       

W1 = W(2:nx+1,2:ny+1,:);    
b=ones(nx,1)*Tinicial;

#funcao 2D
  #for k=1:(nt-1)
    #for j=1:ny
     #for i=1:nx
        #T(2,j,k+1)=deltay*hagua*T(1,j,k+1)+T(1,j,k+1); 
        #T(i,2,k+1)=deltax*hagua*T(i,1,k+1)+T(i,1,k+1);
        #T(i,5,k+1)=(T(i,4,k+1)-deltax*hagua*Tfinal)/(1-deltax*hagua);
        #T(5,j,k+1)=(T(4,j,k+1)-deltay*hagua*Tfinal)/(1-deltay*hagua);
        #T(4,j,k+1)=T(3,j,k+1);
        #T(i,4,k+1)=T(i,3,k+1);
        #T(i,j,k+1)=((T(i,j+1,k) - 2*T(i,j,k) + T(i,j-1,k))/(deltay^2) + (T(i+1,j,k) - 2*T(i,j,k) + T(i-1,j,k))/(deltax^2))*deltat*k_aco/(densidade_aco*calor_esp_aco)+T(i,j,k);
      #endfor
     #endfor
  #endfor
 
  #funcao 1D
  #for k=1:(nt-1)
    #for i=2:(nx-1)
      #T1(i,k+1)=((T1(i+1,k) - 2*T1(i,k) + T1(i-1,k))/(deltax^2) - (area_placa*k_aco*(T1(i+1,k) - T1(i-1,k))/(2*deltax))/k_aco - (area_placa)*har*(T1(i,k)-Tfinal)/k_aco)/(densidade_aco*calor_esp_aco)*deltat+T1(i,k);
     #endfor
   #endfor
   
   
  chamando uma matriz temperatura final hipotetica
  Tverdadeiro=zeros(nx,ny,nt);
  Tverdadeiro(:,:,nt)=Tfinal;
  Tverdadeiro1=zeros(nx,nt);
  Tverdadeiro1(:,nt)=Tfinal;
 
  #testando nosso resultado
  contador1 = 1;
  contador2 = 1;
  contador3 = 1;
  gama=0;
  gama1=0;
  
  while contador1 ~= nx && contador2 ~= ny && contador3 ~= nt
    gama=gama+(T(contador1,contador2,contador3)-Tverdadeiro(contador1,contador2,contador3))^2;
    contador1=contador1+1;
    contador2=contador2+1;
    contador3=contador3+1;
  endwhile
  
  while contador1 ~= nx && contador3 ~= nt
    gama1=gama1+(T1(contador1,contador3)-Tverdadeiro1(contador1,contador3))^2;
    contador1=contador1+1;
    contador3=contador3+1;
  endwhile


  W1 = W(2:nx+1,2:ny+1,:);
  b=ones(nx,1)*Tinicial;
  
  [X,Y]=meshgrid(0:deltax:tamanho_x_placa,0:deltay:tamanho_y_placa);
  
  Tcalc=A\ones((nx+1)*(ny+1),1)*1050+273
  
  [im,jm]=ind2sub([(nx+1) (ny+1)],1:(nx+1)*(ny+1))
  for k=1:(nx+1)*(ny+1)
      Tc(im(k),jm(k))=Tcalc(k);
  end
  
  surf(X,Y,Tc)
  
  contour(X,Y,Tc)

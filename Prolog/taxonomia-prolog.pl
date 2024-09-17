% factos 
filo(cordados,mamiferos).  
filo(cordados,aves).  
filo(cordados,repteis).  
filo(cordados,peixes).  
filo(artropodes,insetos).  
filo(poriferos,demoesponjas).  
classe(mamiferos,carnivora).     
classe(mamiferos,artiodactilos).   
classe(mamiferos,perissodactilos).   
classe(mamiferos,cetaceos).   
classe(aves,pinguins). 
classe(repteis,crocodilianos). 
classe(repteis,escamados).   
classe(peixes,perciformes).   
classe(insetos,lepidoperos).  
classe(demoesponjas,haplosclerida).  
ordem(carnivora,felinos). 
ordem(carnivora,canideos). 
ordem(artiodactilos,elefantes). 
ordem(artiodactilos,girafas). 
ordem(artiodactilos,equidios). 
ordem(perissodactilos,rinocerontes). 
ordem(cetaceos,delfineos). 
ordem(cetaceos,baleias). 
ordem(pinguins,pinguins). 
ordem(crocodilianos,crocodilos). 
ordem(escamados,serpentes). 
ordem(perciformes,peixes-palhaço). 
ordem(lepidoperos,borboletas). 
ordem(haplosclerida,esponjas). 
familia(felinos,gato). 
familia(felinos, leão). 
familia(felinos, tigre). 
familia(canideos, cão). 
familia(elefantes, elefante). 
familia(girafas, girafa). 
familia(equidios, cavalo). 
familia(rinocerontes, rinoceronte). 
familia(delfineos, golfinho). 
familia(baleias, baleia). 
familia(pinguins, pinguim). 
familia(crocodilos,crocodilo). 
familia(crocodilos,jacare). 
familia(serpentes,cobra). 
familia(peixes-palhaço,nemo). 
familia(borboletas,borboleta). 
familia(esponjas,esponaja). 

% Relação
taxonomia(Animal, Familia) :-
    familia(Familia, Animal).

taxonomia(Animal, Ordem) :-
    familia(Familia, Animal),
    ordem(Ordem, Familia).

taxonomia(Animal, Classe) :-
    familia(Familia, Animal),
    ordem(Ordem, Familia),
    classe(Classe, Ordem).

taxonomia(Animal, Filo) :-
    familia(Familia, Animal),
    ordem(Ordem, Familia),
    classe(Classe, Ordem),
    filo(Filo, Classe).

taxonomia(Filo) :-
    familia(Familia, Animal),
    ordem(Ordem, Familia),
    classe(Classe, Ordem),
    format('Animal: ~w~n', [Animal]),
    format('Familia: ~w~n', [Familia]),
    format('Ordem: ~w~n', [Ordem]),
    format('Classe: ~w~n', [Classe]),
    format('Filo: ~w~n --------', [Filo]).

taxonomia(Classe) :-
    familia(Familia, Animal),
    ordem(Ordem, Familia),
    filo(Filo, Classe),
    format('Classe: ~w~n ---------', [Classe]),
    format('Animal: ~w~n', [Animal]),
    format('Familia: ~w~n', [Familia]),
    format('Ordem: ~w~n', [Ordem]),
    format('Filo: ~w~n', [Filo]).

taxonomia(Ordem) :-
    familia(Familia, Animal),
    classe(Classe, Ordem),
    filo(Filo, Classe),
    format('Ordem: ~w~n ---------', [Ordem]),
    format('Animal: ~w~n', [Animal]),
    format('Familia: ~w~n', [Familia]),
    format('Classe: ~w~n', [Classe]),
    format('Filo: ~w~n', [Filo]).

taxonomia(Familia) :-
    familia(Familia, Animal),
    ordem(Ordem, Familia),
    classe(Classe, Ordem),
    filo(Filo, Classe),
    format('Familia: ~w~n ------', [Familia]),
    format('Animal: ~w~n', [Animal]),
    format('Ordem: ~w~n', [Ordem]),
    format('Classe: ~w~n', [Classe]),
    format('Filo: ~w~n', [Filo]).

taxonomia(Animal) :-
    familia(Familia, Animal),
    ordem(Ordem, Familia),
    classe(Classe, Ordem),
    filo(Filo, Classe),
    format('Animal: ~w~n', [Animal]),
    format('Familia: ~w~n', [Familia]),
    format('Ordem: ~w~n', [Ordem]),
    format('Classe: ~w~n', [Classe]),
    format('Filo: ~w~n', [Filo]).


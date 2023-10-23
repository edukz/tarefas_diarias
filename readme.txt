Este código é um aplicativo de gerenciamento de tarefas simples baseado na biblioteca tkinter do Python, para uso pessoal. Desenvolvido para estudo da biblioteca tkinter.


Bibliotecas necessárias: 

tkinter, messagebox e simpledialog.


Funções:

salvar_tarefas(): Salva todas as tarefas da lista de tarefas (lista_tarefas) em um arquivo chamado "tarefas.txt". Cada tarefa é salva em uma nova linha.

carregar_tarefas(): Carrega tarefas do arquivo "tarefas.txt" e as adiciona à lista de tarefas (lista_tarefas). Se o arquivo não existir, essa função não faz nada.

adicionar_tarefa(): Adiciona uma tarefa da caixa de entrada (entrada_tarefa) à lista de tarefas e salva a atualização no arquivo. Se a caixa de entrada estiver vazia, uma mensagem de aviso será exibida.

remover_tarefa(): Remove a tarefa selecionada da lista de tarefas e salva a atualização no arquivo. Se nenhuma tarefa estiver selecionada, uma mensagem de aviso será exibida.

editar_tarefa(): Edita a tarefa selecionada usando uma caixa de diálogo. A tarefa editada substituirá a tarefa anterior e a atualização será salva no arquivo. Se nenhuma tarefa estiver selecionada, uma mensagem de aviso será exibida.

Configuração da Interface Gráfica:

Inicializa a janela principal com o título "Gerenciador de Tarefas Avançado".

Cria e posiciona uma caixa de entrada (entrada_tarefa) para inserir novas tarefas.

Cria e posiciona uma lista (lista_tarefas) onde as tarefas serão exibidas. Esta lista permite ao usuário selecionar uma tarefa para editar ou remover.

Cria e posiciona três botões: "Adicionar Tarefa", "Remover Tarefa" e "Editar Tarefa". Esses botões têm funções associadas a eles, permitindo que o usuário adicione, remova ou edite tarefas, respectivamente.

Execução:

Ao iniciar o programa, a função carregar_tarefas() é chamada para preencher a lista de tarefas com tarefas salvas anteriormente (se existirem).

Finalmente, app.mainloop() é chamado para iniciar o loop principal do tkinter, exibindo a interface gráfica e esperando por ações do usuário.
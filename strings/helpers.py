HELP_1 = """<b><u>Comandos admin:</b></u>

Basta adicionar <b>c</b> no início dos comandos para usá-los para canal.

/pause : Pausar música/vídeo atual.
/resume : Retomar música/vídeo atual.
/skip : Pular música/vídeo atual.
/end ou /stop : Limpa a fila e encerra a transmissão atual.
/player : Exibir painel interativo do player.
/queue : Exibir lista de reprodução.
/lyrics [nome da música] : Pesquise as letras da música solicitada e os resultados.
"""

HELP_2 = """
<b><u>Usuários autorizados:</b></u>

Usuários autorizados ganham permissão de administrador no bot sem permissão de administrador no grupo.

/auth [usuário/id] : Adicionar usuário à lista de autorizados.
/unauth [usuário/id] : Remover usuário à lista de autorizados.
/authusers : Exibir lista de usuários autorizados.
"""

HELP_3 = """
<u><b>Recurso de transmissão</b></u> [apenas para membros do COMBINADO]:

/broadcast [Mensagem ou resposta de mensagem] : Transmitir uma mensagem para grupos que o bot está.

<u>Modos de transmissão:</u>
<b>-pin</b> : Fixar suas mensagens transmitidas pelo bot em grupos que o bot está.
<b>-pinloud</b> : Fixar suas mensagens transmitidas pelo bot em grupos que o bot está e notifica os usuários.
<b>-user</b> : Transmita a mensagem para os usuários que iniciaram o bot.
<b>-assistant</b> : Transmita sua mensagem da conta assistente do bot.
<b>-nobot</b> : Força o bot a não transmitir a mensagem.

<b>Exemplo:</b> <code>/broadcast -user -assistant -pin Salve fudidos, tomanocu geral!</code>
"""

HELP_4 = """<u><b>Recurso de lista negra de grupo</b></u> [apenas para membros do COMBINADO]:

Restrinja grupos de merda para usar nosso precioso bot.

/blacklistchat [ID do grupo] : Adiciona grupo à lista negra de uso do bot.
/whitelistchat [ID do grupo] : Remove grupo da lista negra de uso do bot.
/blacklistedchat : Exibir grupos da lista negra.
"""

HELP_5 = """
<u><b>Bloquear usuários</b></u> [apenas para membros do COMBINADO]:

Começa a ignorar o usuário na lista negra, para que ele não possa usar comandos do bot.

/block [usuário ou responda uma mensagem do usuário] : Bloquear usuário do bot.
/unblock [usuário ou responda uma mensagem do usuário] : Desbloquear usuário do bot.
/blockedusers : Exibir lista de usuários bloqueados.
"""

HELP_6 = """
<u><b>Comandos de reprodução:</b></u>

O bot consegue transmitir áudio e vídeo na call do grupo.

/cplay : Inicia a transmissão da música solicitada no grupo.
/cvplay : Inicia a transmissão do vídeo solicitada no grupo.
/cplayforce ou /cvplayforce : Interrompe o streaming em andamento e inicia o streaming da faixa solicitada.
/channelplay [Nome do grupo ou ID] ou [disable] : Conecte o canal a um grupo e iniciar a transmissão de faixas com a ajuda de comandos enviados em grupo.
"""

HELP_7 = """
<u><b>Recurso de ban global</b></u> [apenas para membros do COMBINADO]:

/gban [usuário ou responda uma mensagem do usuário] : Proíbe globalmente o usuário de todos os bate-papos que o bot está e o coloca na lista negra de usar o bot.
/ungban [usuário ou responda uma mensagem do usuário] : Remove o ban global do usuário de todos os bate-papos que o bot está e remove da lista negra de usar o bot.
/gbannedusers : Exibir lista dos usuários banidos globalmente.
"""

HELP_8 = """
<b><u>Repetição de faixas:</b></u>

<b>Inicia a transmissão do fluxo contínuo em loop.</b>

/loop [enable/disable] : Ativar/desativar repetição de faixas.
/loop [1, 2, 3, ...] : Repetir faixas quantas vezes você estabelecer.
"""

HELP_9 = """
<u><b>Modo manutenção</b></u> [apenas para membros do COMBINADO]:

/logs : Exibir logs do bot.
/logger [enable/disable] : O bot começará a registrar os logs que acontecem no bot.
/maintenance [enable/disable] : Ativar/desativar modo manutenção do bot.
"""

HELP_10 = """
<b><u>Ping e status:</b></u>

/start : Iniciar o bot de música.
/help : Exibir menu de ajuda com explicação dos comandos.
/ping : Exibir ping e estatísticas do sistema.
/stats : Mostra as estatísticas gerais do bot.
"""

HELP_11 = """
<u><b>Comandos de reprodução:</b></u>

<b>v :</b> Significa reprodução de vídeo.
<b>force :</b> Significa forçar reprodução.

/play ou /vplay : Inicia reprodução de áudio.
/playforce ou /vplayforce : Remove reprodução atual e inicia reprodução do novo áudio solicitado.
"""

HELP_12 = """
<b><u>Fila aleatória:</b></u>

/shuffle : Embaralhar a fila atual.
/queue : Mostra a fila embaralhada.
"""

HELP_13 = """
<b><u>Avançar e retroceder:</b></u>

Você pode avançar ou retroceder quantos segundos quiser do que estiver reproduzindo na call.

/seek [duração em segundos] : Avança transmissão em quantos segundos for determinado.
/seekback [duração em segundos] : Retrocede transmissão em quantos segundos for determinado.
"""

HELP_14 = """
<b><u>Baixar música:</b></u>

/song [nume/link YouTube] : Baixe qualquer faixa do YouTube nos formatos mp3 ou mp4.
"""

HELP_15 = """
<b><u>Comandos de velocidade:</b></u>

Você pode controlar a velocidade de reprodução do stream em andamento. [Apenas administradores do grupo]

/speed ou /playback : Ajustar a velocidade de reprodução de áudio no grupo.
/cspeed ou /cplayback : Ajustar a velocidade de reprodução de áudio no canal.
"""

HELP_16 = """
<b><u>Marcações:</b></u>

Você pode mencionar todos os membros do grupo para passar algum recado. [Apenas administradores do grupo]

@all [mensagem] : Iniciar processo de marcações, marcando 5 membros do grupo a cada mensagem.
/cancel : Interromper processo de marcações atual.

<b>Exemplo:</b> <code>@all Vem pra call seus fudidos!</code>
"""

import pygame
import time

# Inisialisasi pygame
pygame.init()

# Setting window
width = 800
height = 600
window = pygame.display.set_mode((width, height))

# Setting warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Membuat fungsi untuk melakukan gerakan dumbbell crunches
def dumbbell_crunches():
    font = pygame.font.Font(None, 30)
    text = font.render("Posisi awal: Berbaring telentang di atas matras dengan kedua kaki ditekuk dan telapak kaki di tanah. Pegang dumbbell dengan kedua tangan dan letakkan di atas dada.", True, BLACK)
    window.blit(text, (50, 50))
    pygame.display.update()
    time.sleep(3)

    text = font.render("Angkat bahu dan kepala dari matras dengan menekuk tulang rusuk ke arah panggul. Pada saat yang sama, angkat dumbbell dari dada dan perlahan-lahan arahkan ke atas ke arah lutut. Tahan selama satu detik pada puncak gerakan.", True, BLACK)
    window.blit(text, (50, 100))
    pygame.display.update()
    time.sleep(3)

    text = font.render("Perlahan turunkan tubuh kembali ke posisi awal dengan kontrol.", True, BLACK)
    window.blit(text, (50, 150))
    pygame.display.update()
    time.sleep(3)

# Main loop
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    # Setting background color
    window.fill(WHITE)

    # Panggil fungsi dumbbell crunches
    dumbbell_crunches()

    pygame.display.update()

# Quit pygame
pygame.quit()
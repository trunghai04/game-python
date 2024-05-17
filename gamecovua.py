# Khởi tạo module pygame
import pygame
import pygame.transform

hinh_anh_hau_trang = pygame.image.load('./images/hau_trang.png')
hinh_anh_hau_trang = pygame.transform.scale(hinh_anh_hau_trang, (80, 80))
hinh_anh_hau_trang_nho = pygame.transform.scale(hinh_anh_hau_trang, (45, 45))
hinh_anh_tot_den_nho = pygame.transform.scale(hinh_anh_tot_den, (45, 45))

board = pygame.image.load('./images/chess_board.jpg')

board = pygame.transform.scale(board, (800, 800))

# Hàm vẽ bàn cờ chính của trò chơi

def ve_ban_co():

    screen.blit(board, (0, 0))

# Hàm vẽ các quân cờ trên bàn cờ

def ve_quan_co():

    for i in range(len(white_pieces)):

        if white_pieces[i] == 'hậu':

            screen.blit(hinh_anh_hau_trang, (white_locations[i][0] * 100, white_locations[i][1] * 100))

        if white_pieces[i] == 'vua':

            screen.blit(hinh_anh_vua_trang, (white_locations[i][0] * 100, white_locations[i][1] * 100))

        if white_pieces[i] == 'xe':

            screen.blit(hinh_anh_xe_trang, (white_locations[i][0] * 100, white_locations[i][1] * 100))

        if white_pieces[i] == 'tượng':

            screen.blit(hinh_anh_tuong_trang, (white_locations[i][0] * 100, white_locations[i][1] * 100))

        if white_pieces[i] == 'ma':

            screen.blit(hinh_anh_ma_trang, (white_locations[i][0] * 100, white_locations[i][1] * 100))

        if white_pieces[i] == 'tốt':

            screen.blit(hinh_anh_tot_trang, (white_locations[i][0] * 100, white_locations[i][1] * 100))

    for i in range(len(black_pieces)):

        if black_pieces[i] == 'hậu':

            screen.blit(hinh_anh_hau_den, (black_locations[i][0] * 100, black_locations[i][1] * 100))

        if black_pieces[i] == 'vua':

            screen.blit(hinh_anh_vua_den, (black_locations[i][0] * 100, black_locations[i][1] * 100))

        if black_pieces[i] == 'xe':

            screen.blit(hinh_anh_xe_den, (black_locations[i][0] * 100, black_locations[i][1] * 100))

        if black_pieces[i] == 'tượng':

            screen.blit(hinh_anh_tuong_den, (black_locations[i][0] * 100, black_locations[i][1] * 100))

        if black_pieces[i] == 'ma':

            screen.blit(hinh_anh_ma_den, (black_locations[i][0] * 100, black_locations[i][1] * 100))

        if black_pieces[i] == 'tốt':

            screen.blit(hinh_anh_tot_den, (black_locations[i][0] * 100, black_locations[i][1] * 100))
def kiem_tra_hau(x, y):

    hau = []

    c = 1

    while x + c < 8 and y + c < 8:

        if (x + c, y + c) in white_locations:

            break

        hau.append((x + c, y + c))

        if (x + c, y + c) in black_locations:

            break

        c += 1

    c = 1

    while x + c < 8 and y - c >= 0:

        if (x + c, y - c) in white_locations:

            break

        hau.append((x + c, y - c))

        if (x + c, y - c) in black_locations:

            break

        c += 1

    c = 1

    while x - c >= 0 and y + c < 8:

        if (x - c, y + c) in white_locations:

            break

        hau.append((x - c, y + c))

        if (x - c, y + c) in black_locations:

            break

        c += 1

    c = 1

    while x - c >= 0 and y - c >= 0:

        if (x - c, y - c) in white_locations:

            break

        hau.append((x - c, y - c))

        if (x - c, y - c) in black_locations:

            break

        c += 1

    c = 1

    while x + c < 8:

        if (x + c, y) in white_locations:

            break

        hau.append((x + c, y))

        if (x + c, y) in black_locations:

            break

        c += 1

    c = 1

    while x - c >= 0:

        if (x - c, y) in white_locations:

            break

        hau.append((x - c, y))

        if (x - c, y) in black_locations:

            break

        c += 1

    c = 1

    while y + c < 8:

        if (x, y + c) in white_locations:

            break

        hau.append((x, y + c))

        if (x, y + c) in black_locations:

            break

        c += 1

    c = 1

    while y - c >= 0:

        if (x, y - c) in white_locations:

            break

        hau.append((x, y - c))

        if (x, y - c) in black_locations:

            break

        c += 1

    return hau

def kiem_tra_vua(x, y):

    vua = []

    if x - 1 >= 0:

        vua.append((x - 1, y))

    if x + 1 < 8:

        vua.append((x + 1, y))

    if y - 1 >= 0:

        vua.append((x, y - 1))

    if y + 1 < 8:

        vua.append((x, y + 1))

    if x + 1 < 8 and y + 1 < 8:

        vua.append((x + 1, y + 1))

    if x - 1 >= 0 and y - 1 >= 0:

        vua.append((x - 1, y - 1))

    if x - 1 >= 0 and y + 1 < 8:

        vua.append((x - 1, y + 1))

    if x + 1 < 8 and y - 1 >= 0:

        vua.append((x + 1, y - 1))

    return vua

def kiem_tra_xe(x, y):

    xe = []

    c = 1

    while x + c < 8:

        if (x + c, y) in white_locations:

            break

        xe.append((x + c, y))

        if (x + c, y) in black_locations:

            break

        c += 1

    c = 1

    while x - c >= 0:

        if (x - c, y) in white_locations:

            break

        xe.append((x - c, y))

        if (x - c, y) in black_locations:

            break

        c += 1

    c = 1

    while y + c < 8:

        if (x, y + c) in white_locations:

            break

        xe.append((x, y + c))

        if (x, y + c) in black_locations:

            break

        c += 1

    c = 1

    while y - c >= 0:

        if (x, y - c) in white_locations:

            break

        xe.append((x, y - c))

        if (x, y - c) in black_locations:

            break

        c += 1

    return xe

def kiem_tra_tuong(x, y):

    tuong = []

    if x + 1 < 8 and y + 1 < 8:

        tuong.append((x + 1, y + 1))

    if x - 1 >= 0 and y + 1 < 8:

        tuong.append((x - 1, y + 1))

    if x + 1 < 8 and y - 1 >= 0:

        tuong.append((x + 1, y - 1))

    if x - 1 >= 0 and y - 1 >= 0:

        tuong.append((x - 1, y - 1))

    return tuong

def kiem_tra_ma(x, y):

    ma = []

    if x + 2 < 8 and y + 1 < 8:

        ma.append((x + 2, y + 1))

    if x - 2 >= 0 and y + 1 < 8:

        ma.append((x - 2, y + 1))

    if x + 2 < 8 and y - 1 >= 0:

        ma.append((x + 2, y - 1))

    if x - 2 >= 0 and y - 1 >= 0:

        ma.append((x - 2, y - 1))

    if x + 1 < 8 and y + 2 < 8:

        ma.append((x + 1, y + 2))

    if x - 1 >= 0 and y + 2 < 8:

        ma.append((x - 1, y + 2))

    if x + 1 < 8 and y - 2 >= 0:

        ma.append((x + 1, y - 2))

    if x - 1 >= 0 and y - 2 >= 0:

        ma.append((x - 1, y - 2))

    return ma

def kiem_tra_tot(x, y, mau):

    if mau == 'trang':

        if (x, y - 1) not in black_locations and (x, y - 1) not in white_locations:

            tot = [(x, y - 1)]

        else:

            tot = []

        if y == 6 and (x, y - 1) not in black_locations and (x, y - 1) not in white_locations and (x, y - 2) not in black_locations and (x, y - 2) not in white_locations:

            tot.append((x, y - 2))

    else:

        if (x, y + 1) not in black_locations and (x, y + 1) not in white_locations:

            tot = [(x, y + 1)]

        else:

            tot = []

        if y == 1 and (x, y + 1) not in black_locations and (x, y + 1) not in white_locations and (x, y + 2) not in black_locations and (x, y + 2) not in white_locations:

            tot.append((x, y + 2))

    return tot
def kiem_tra_quan(x, y):

    for i in range(len(white_locations)):

        if white_locations[i] == (x, y):

            if white_pieces[i] == 'hậu':

                return kiem_tra_hau(x, y)

            if white_pieces[i] == 'vua':

                return kiem_tra_vua(x, y)

            if white_pieces[i] == 'xe':

                return kiem_tra_xe(x, y)

            if white_pieces[i] == 'tượng':

                return kiem_tra_tuong(x, y)

            if white_pieces[i] == 'ma':

                return kiem_tra_ma(x, y)

            if white_pieces[i] == 'tốt':

                return kiem_tra_tot(x, y, 'trang')

    for i in range(len(black_locations)):

        if black_locations[i] == (x, y):

            if black_pieces[i] == 'hậu':

                return kiem_tra_hau(x, y)

            if black_pieces[i] == 'vua':

                return kiem_tra_vua(x, y)

            if black_pieces[i] == 'xe':

                return kiem_tra_xe(x, y)

            if black_pieces[i] == 'tượng':

                return kiem_tra_tuong(x, y)

            if black_pieces[i] == 'ma':

                return kiem_tra_ma(x, y)

            if black_pieces[i] == 'tốt':

                return kiem_tra_tot(x, y, 'den')

    return []

# Kiểm tra xem vị trí (x, y) có nằm trong danh sách các vị trí hợp lệ không

def kiem_tra_hop_le(x, y, danh_sach_hop_le):

    for i in range(len(danh_sach_hop_le)):

        if (x, y) == danh_sach_hop_le[i]:

            return True

    return False

# Kiểm tra xem vị trí (x, y) có nằm trong danh sách các vị trí địch không

def kiem_tra_quan_dich(x, y, mau):

    if mau == 'trang':

        for i in range(len(black_locations)):

            if (x, y) == black_locations[i]:

                return True

    else:

        for i in range(len(white_locations)):

            if (x, y) == white_locations[i]:

                return True

    return False
# Hàm kiểm tra xem người chơi nào chiến thắng

def kiem_tra_thang():

    if (4, 0) in white_locations:

        if kiem_tra_quan(4, 0) == [] and kiem_tra_quan(3, 0) == [] and kiem_tra_quan(5, 0) == [] and kiem_tra_quan(2, 0) == [] and kiem_tra_quan(6, 0) == []:

            return 'đen'

    if (4, 7) in black_locations:

        if kiem_tra_quan(4, 7) == [] and kiem_tra_quan(3, 7) == [] and kiem_tra_quan(5, 7) == [] and kiem_tra_quan(2, 7) == [] and kiem_tra_quan(6, 7) == []:

            return 'trang'

    return 'chua'

# Hàm xử lý khi một ván chơi kết thúc

def ket_thuc(van_chua):

    screen.fill((255, 255, 255))

    # Hiển thị thông báo chiến thắng

    if van_chua == 'trang':

        text = big_font.render('Người chơi Trắng chiến thắng!', True, (0, 0, 0))

    else:

        text = big_font.render('Người chơi Đen chiến thắng!', True, (0, 0, 0))

    textRect = text.get_rect()

    textRect.center = (WIDTH // 2, HEIGHT // 2)

    screen.blit(text, textRect)

    pygame.display.update()

    pygame.time.delay(3000)

    pygame.quit()

# Hàm xử lý khi trò chơi đang diễn ra

def van_dang_choi():

    global selection, valid_moves, turn_step

    screen.fill((255, 255, 255))

    ve_ban_co()

    ve_quan_co()

    # Hiển thị lượt của người chơi

    if turn_step == 0 or turn_step == 2:

        text = font.render('Lượt người chơi Trắng', True, (0, 0, 0))

    else:

        text = font.render('Lượt người chơi Đen', True, (0, 0, 0))

    screen.blit(text, (10, 10))

    # Hiển thị quân cờ được chọn

    if selection != 100:

        pygame.draw.rect(screen, (255, 0, 0), (selection[0] * 100, selection[1] * 100, 100, 100), 4)

    # Hiển thị các nước đi hợp lệ

    for move in valid_moves:

        pygame.draw.circle(screen, (0, 255, 0), (move[0] * 100 + 50, move[1] * 100 + 50), 10)
        # Hàm chính xử lý trò chơi

def choi_co_vua():

    global selection, valid_moves, turn_step, captured_pieces_white, captured_pieces_black

    van_chua = 'chua'

    running = True

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                running = False

                break

            if turn_step == 0:

                if event.type == pygame.MOUSEBUTTONDOWN:

                    x, y = pygame.mouse.get_pos()

                    x = x // 100

                    y = y // 100

                    for i in range(len(white_locations)):

                        if white_locations[i] == (x, y):

                            selection = (x, y)

                            valid_moves = kiem_tra_quan(x, y)

                            turn_step = 1

                            break

            elif turn_step == 1:

                if event.type == pygame.MOUSEBUTTONDOWN:

                    x, y = pygame.mouse.get_pos()

                    x = x // 100

                    y = y // 100

                    if kiem_tra_kiem_tra_quan_vua_hop_le(x, y, 'trang', white_locations):

                        valid_moves = []

                        selection = 100

                        turn_step = 2

                        continue

                    if kiem_tra_hop_le(x, y, valid_moves):

                        for i in range(len(white_locations)):

                            if white_locations[i] == selection:

                                if white_pieces[i] != 'tốt' and x == 0 and mau == 'trang':

                                    captured_pieces_black.append(black_pieces[i])

                                if white_pieces[i] != 'tốt' and x == 7 and mau == 'trang':

                                    captured_pieces_black.append(black_pieces[i])

                                if white_pieces[i] == 'vua':

                                    vua_index = i

                                white_locations[i] = (x, y)

                        selection = 100

                        valid_moves = []

                        # Kiểm tra thắng thua

                        van_chua = kiem_tra_thang()

                        if van_chua != 'chua':

                            ket_thuc(van_chua)

                        turn_step = 2

            elif turn_step == 2:

                if event.type == pygame.MOUSEBUTTONDOWN:

                    x, y = pygame.mouse.get_pos()

                    x = x // 100

                    y = y // 100

                    for i in range(len(black_locations)):

                        if black_locations[i] == (x, y):

                            selection = (x, y)

                            valid_moves = kiem_tra_quan(x, y)

                            turn_step = 3

                            break

            elif turn_step == 3:

                if event.type == pygame.MOUSEBUTTONDOWN:

                    x, y = pygame.mouse.get_pos()

                    x = x // 100

                    y = y // 100

                    if kiem_tra_kiem_tra_quan_vua_hop_le(x, y, 'den', black_locations):

                        valid_moves = []

                        selection = 100

                        turn_step = 0

                        continue

                    if kiem_tra_hop_le(x, y, valid_moves):

                        for i in range(len(black_locations)):

                            if black_locations[i] == selection:

                                if black_pieces[i] != 'tốt' and x == 0 and mau == 'den':

                                    captured_pieces_white.append(white_pieces[i])

                                if black_pieces[i] != 'tốt' and x == 7 and mau == 'den':

                                    captured_pieces_white.append(white_pieces[i])

                                if black_pieces[i] == 'vua':

                                    vua_index = i

                                black_locations[i] = (x, y)

                        selection = 100

                        valid_moves = []

                        # Kiểm tra thắng thua

                        van_chua = kiem_tra_thang()

                        if van_chua != 'chua':

                            ket_thuc(van_chua)

                        turn_step = 0

        # Vẽ bàn cờ và quân cờ

        van_dang_choi()

        # Hiển thị danh sách quân cờ đã bị bắt

        for i in range(len(captured_pieces_white)):

            screen.blit(hinh_anh_tuong_den_nho, (100 * i, 800))

        for i in range(len(captured_pieces_black)):

            screen.blit(hinh_anh_tuong_trang_nho, (100 * i, 900))

        pygame.display.update()

        timer.tick(fps)

# Bắt đầu trò chơi

choi_co_vua()

# Kết thúc trò chơi

pygame.quit()

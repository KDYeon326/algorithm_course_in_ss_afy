import sys
input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    n = int(input().strip())
    cmds = input().split()

    # 6개 면 초기화 (각 면은 3x3)
    U = [['w'] * 3 for _ in range(3)]
    D = [['y'] * 3 for _ in range(3)]
    F = [['r'] * 3 for _ in range(3)]
    B = [['o'] * 3 for _ in range(3)]
    L = [['g'] * 3 for _ in range(3)]
    R = [['b'] * 3 for _ in range(3)]

    for c in cmds:
        side, direct = c[0], c[1]

        if side == 'U':
            target = U
        elif side == 'D':
            target = D
        elif side == 'F':
            target = F
        elif side == 'B':
            target = B
        elif side == 'L':
            target = L
        else:
            target = R

        temp_face = [row[:] for row in target]

        if direct == '+':  # 시계 90도
            target[0][0], target[0][1], target[0][2] = temp_face[2][0], temp_face[1][0], temp_face[0][0]
            target[1][0], target[1][1], target[1][2] = temp_face[2][1], temp_face[1][1], temp_face[0][1]
            target[2][0], target[2][1], target[2][2] = temp_face[2][2], temp_face[1][2], temp_face[0][2]
        else:  # 반시계 90도
            target[0][0], target[0][1], target[0][2] = temp_face[0][2], temp_face[1][2], temp_face[2][2]
            target[1][0], target[1][1], target[1][2] = temp_face[0][1], temp_face[1][1], temp_face[2][1]
            target[2][0], target[2][1], target[2][2] = temp_face[0][0], temp_face[1][0], temp_face[2][0]

        # ==========================================
        # 2. 인접 면 회전 (Side Rotation)
        # ==========================================
        # 규칙: 영향을 받는 4개 면의 줄(Strip)을 미리 다 뽑아둠 (Read)
        # 그 다음 방향에 맞춰 한 번에 대입함 (Write)

        if side == 'U':
            # U면 주변: F(윗줄), R(윗줄), B(윗줄), L(윗줄)
            s_F = F[0][:]  # 복사본 생성
            s_R = R[0][:]
            s_B = B[0][:]
            s_L = L[0][:]

            if direct == '+':  # F -> L -> B -> R -> F
                F[0], L[0], B[0], R[0] = s_R, s_F, s_L, s_B
            else:  # F -> R -> B -> L -> F
                F[0], R[0], B[0], L[0] = s_L, s_F, s_R, s_B

        elif side == 'D':
            # D면 주변: F(아랫줄), R(아랫줄), B(아랫줄), L(아랫줄)
            s_F = F[2][:]
            s_R = R[2][:]
            s_B = B[2][:]
            s_L = L[2][:]

            if direct == '+':  # F -> R -> B -> L -> F (D는 위에서 볼때랑 회전방향 반대 영향)
                F[2], R[2], B[2], L[2] = s_L, s_F, s_R, s_B
            else:
                F[2], L[2], B[2], R[2] = s_R, s_F, s_L, s_B

        elif side == 'F':
            # F면 주변: U(아랫줄), R(왼쪽줄), D(윗줄), L(오른쪽줄)
            s_U = U[2][:]
            s_R = [R[0][0], R[1][0], R[2][0]]
            s_D = D[0][:]
            s_L = [L[0][2], L[1][2], L[2][2]]

            if direct == '+':  # U->R, R->D, D->L, L->U
                # U[2] <- L(위로 뒤집힘)
                U[2] = [s_L[2], s_L[1], s_L[0]]
                # R[col 0] <- U
                for i in range(3): R[i][0] = s_U[i]
                # D[0] <- R(뒤집힘)
                D[0] = [s_R[2], s_R[1], s_R[0]]
                # L[col 2] <- D
                for i in range(3): L[i][2] = s_D[i]
            else:
                # U[2] <- R
                U[2] = [s_R[0], s_R[1], s_R[2]]
                # L[col 2] <- U(뒤집힘)
                for i in range(3): L[i][2] = s_U[2 - i]
                # D[0] <- L
                D[0] = [s_L[0], s_L[1], s_L[2]]
                # R[col 0] <- D(뒤집힘)
                for i in range(3): R[i][0] = s_D[2 - i]

        elif side == 'B':
            # B면 주변: U(윗줄), L(왼쪽줄), D(아랫줄), R(오른쪽줄)
            s_U = U[0][:]
            s_L = [L[0][0], L[1][0], L[2][0]]
            s_D = D[2][:]
            s_R = [R[0][2], R[1][2], R[2][2]]

            if direct == '+':  # U->L, L->D, D->R, R->U
                # U[0] <- R
                U[0] = [s_R[0], s_R[1], s_R[2]]
                # L[col 0] <- U(뒤집힘)
                for i in range(3): L[i][0] = s_U[2 - i]
                # D[2] <- L
                D[2] = [s_L[0], s_L[1], s_L[2]]
                # R[col 2] <- D(뒤집힘)
                for i in range(3): R[i][2] = s_D[2 - i]
            else:
                # U[0] <- L(뒤집힘)
                U[0] = [s_L[2], s_L[1], s_L[0]]
                # R[col 2] <- U
                for i in range(3): R[i][2] = s_U[i]
                # D[2] <- R(뒤집힘)
                D[2] = [s_R[2], s_R[1], s_R[0]]
                # L[col 0] <- D
                for i in range(3): L[i][0] = s_D[i]

        elif side == 'L':
            # L면 주변: U(왼쪽줄), F(왼쪽줄), D(왼쪽줄), B(오른쪽줄)
            s_U = [U[0][0], U[1][0], U[2][0]]
            s_F = [F[0][0], F[1][0], F[2][0]]
            s_D = [D[0][0], D[1][0], D[2][0]]
            s_B = [B[0][2], B[1][2], B[2][2]]  # B는 뒷면이라 오른쪽줄이 L과 닿음(전개도상)

            if direct == '+':  # U->F->D->B->U
                # U[col 0] <- B(뒤집힘)
                for i in range(3): U[i][0] = s_B[2 - i]
                # F[col 0] <- U
                for i in range(3): F[i][0] = s_U[i]
                # D[col 0] <- F
                for i in range(3): D[i][0] = s_F[i]
                # B[col 2] <- D(뒤집힘)
                for i in range(3): B[i][2] = s_D[2 - i]
            else:
                # U[col 0] <- F
                for i in range(3): U[i][0] = s_F[i]
                # B[col 2] <- U(뒤집힘)
                for i in range(3): B[i][2] = s_U[2 - i]
                # D[col 0] <- B(뒤집힘)
                for i in range(3): D[i][0] = s_B[2 - i]
                # F[col 0] <- D
                for i in range(3): F[i][0] = s_D[i]

        elif side == 'R':
            # R면 주변: U(오른쪽줄), B(왼쪽줄), D(오른쪽줄), F(오른쪽줄)
            s_U = [U[0][2], U[1][2], U[2][2]]
            s_B = [B[0][0], B[1][0], B[2][0]]  # B는 뒷면이라 왼쪽줄이 R과 닿음
            s_D = [D[0][2], D[1][2], D[2][2]]
            s_F = [F[0][2], F[1][2], F[2][2]]

            if direct == '+':  # U->B->D->F->U
                # U[col 2] <- F
                for i in range(3): U[i][2] = s_F[i]
                # B[col 0] <- U(뒤집힘)
                for i in range(3): B[i][0] = s_U[2 - i]
                # D[col 2] <- B(뒤집힘)
                for i in range(3): D[i][2] = s_B[2 - i]
                # F[col 2] <- D
                for i in range(3): F[i][2] = s_D[i]
            else:
                # U[col 2] <- B(뒤집힘)
                for i in range(3): U[i][2] = s_B[2 - i]
                # F[col 2] <- U
                for i in range(3): F[i][2] = s_U[i]
                # D[col 2] <- F
                for i in range(3): D[i][2] = s_F[i]
                # B[col 0] <- D(뒤집힘)
                for i in range(3): B[i][0] = s_D[2 - i]

    for row in U:
        print("".join(row))
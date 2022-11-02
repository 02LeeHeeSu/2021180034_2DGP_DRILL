from pico2d import *

# 이벤트 정의
RD, LD, RU, LU, TIMER, AD = range(6)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU,
    (SDL_KEYDOWN, SDLK_a): AD
}


# 클래스를 이용해서 상태를 만든다
class IDLE:
    @staticmethod
    def enter(self, event):
        self.dir = 0
        # 타이머 설정
        self.timer = 1000

    @staticmethod
    def exit(self):
        pass

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8

        self.timer -= 1
        if self.timer == 0: # 시간이 경과하면
            # 이벤트 발생.
            # self.queue.insert(0, TIMER)
            # 이 코드는 객체 지향 프로그래밍에 위배된다. 큐에 직접 접근하므로
            self.add_event(TIMER)

    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)


class RUN:
    @staticmethod
    def enter(self, event):
        # self.dir을 결정해야 한다
        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1

    @staticmethod
    def exit(self):
        # run을 나가서 idle 상태로 갈 때, run의 방향을 알려줄 필요가 있다.
        self.face_dir = self.dir

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        self.x = clamp(0, self.x, 800)

    @staticmethod
    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)


class SLEEP:
    @staticmethod
    def enter(self, event):
        self.dir = 0

    @staticmethod
    def exit(self):
        pass

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8

    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            self.image.clip_composite_draw(self.frame * 100, 300, 100, 100,
                                           3.141592 / 2, '',
                                           self.x - 25, self.y - 25, 100, 100)
        else:
            self.image.clip_composite_draw(self.frame * 100, 300, 100, 100,
                                           -3.141592 / 2, '',
                                           self.x - 25, self.y - 25, 100, 100)


class AUTO_RUN:
    @staticmethod
    def enter(self, event):
        if self.face_dir == 1:
            self.dir += 1
        elif self.face_dir == -1:
            self.dir -= 1


    @staticmethod
    def exit(self):
        # auto_run을 나가서 idle, run 상태로 갈 때, run의 방향을 알려줄 필요가 있다.
        self.face_dir = self.dir

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        self.x = clamp(0, self.x, 800)
        if self.x == 800:
            self.dir = -1
        elif self.x == 0:
            self.dir = 1

    @staticmethod
    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)


next_state = {
    IDLE: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, TIMER: SLEEP, AD: AUTO_RUN},
    RUN: {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE, AD: AUTO_RUN},
    SLEEP: {RU: RUN, LU: RUN, RD: RUN, LD: RUN},
    AUTO_RUN: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, AD: IDLE}
}


class Boy:

    def add_event(self, event):
        self.queue.insert(0, event)

    def handle_event(self, event):  # 소년이 스스로 이벤트를 처리할 수 있도록 함
        # event는 키 이벤트.. 이것을 내부 이벤트 테이블의 키로 변환
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('animation_sheet.png')

        self.queue = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)

        if self.queue:
            event = self.queue.pop()
            self.cur_state.exit(self)
            self.cur_state = next_state[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)

class Page(object):
    def __init__(self, totle_data, current_page, page_url, page_count=7, peer_count=10):
        self.totle_data = totle_data
        self.current_page = current_page
        self.page_count = page_count
        self.peer_count = peer_count
        self.page_url = page_url

    @property
    def start(self):
        return (self.current_page - 1) * self.peer_count

    @property
    def end(self):
        return self.current_page * self.peer_count

    @property
    def totle_page(self):
        """计算总页面数"""
        v, y = divmod(self.totle_data, self.peer_count)
        if y:
            v += 1
        return v

    @property
    def choose_page(self):

        # 总页面数小于或等于底部显示的页面数子
        if self.totle_page <= self.page_count:
            start_index = 1
            end_index = self.totle_page + 1
        else:
            # 当前页面接近首页时
            if self.current_page <= (self.page_count + 1) / 2:
                start_index = 1
                end_index = self.page_count + 1

            # 当前页面接近尾页时
            elif self.current_page >= self.totle_page - (self.page_count - 1) / 2:
                start_index = self.totle_page - self.page_count - 1
                end_index = self.totle_page + 1

            else:
                start_index = self.current_page - (self.page_count - 1) / 2
                end_index = self.current_page + (self.page_count + 1) / 2
        return start_index, end_index

    @property
    def prev_page(self):
        prev_page_list = []
        if self.current_page == 1:
            prev = '<a class="page_num" href="javascript:void(0);">上一页</a>'
        else:
            prev = '<a class="page_num" href="%s?p=%s">上一页</a>' % (
                self.page_url,
                int(self.current_page - 1),
            )
        prev_page_list.append(prev)
        return prev_page_list

    @property
    def middle_page(self):
        middle_page_list = []
        for i in range(int(self.choose_page[0]), int(self.choose_page[1])):
            if self.current_page == i:
                temp = '<a class="page_num active" href="%s?p=%s">%s</a>' % (
                    self.page_url,
                    i,
                    i,
                )
            else:
                temp = '<a class="page_num" href="%s?p=%s">%s</a>' % (
                    self.page_url,
                    i,
                    i,
                )
            middle_page_list.append(temp)
        return middle_page_list

    @property
    def after_page(self):
        after_page_list = []
        if self.current_page == self.totle_page:
            next_page = '<a class="page_num" href="javascript:void(0);">下一页</a>'
        else:
            next_page = '<a class="page_num" href="%s?p=%s">下一页</a>' % (
                self.page_url,
                int(self.current_page + 1),
            )
        after_page_list.append(next_page)
        return after_page_list

    @property
    def jump_page(self):
        jump_page_list = []
        jump = (
            """
            <input type="text" /><a onclick='jumpTo(this,"%s?p=");' id="ii1">GO</a>
            <script>
                function jumpTo(ths,base) {
                    var val = ths.previousSibling.value;
                    console.log(val);
                    location.href = base + val;
                }
            </script>
        """
            % self.page_url
        )
        jump_page_list.append(jump)
        return jump_page_list

    @property
    def return_page_str(self):
        prev_page_str = "".join(self.prev_page)
        middle_page_str = "".join(self.middle_page)
        after_page_str = "".join(self.after_page)
        jump_str = "".join(self.jump_page)
        page_str = prev_page_str + middle_page_str + after_page_str + jump_str
        return page_str

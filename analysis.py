# -*- coding:utf-8 -*-


# xlrd==1.2.0
# xlwt==1.3.0
import xlrd
import xlwt
from decimal import Decimal

# self_ = xlrd.open_workbook('c:\\Users\\zhangyunlong\\Desktop\\哈哈哈.xlsx').sheet_by_index(0)
# other = xlrd.open_workbook('c:\\Users\\zhangyunlong\\Desktop\\哈哈哈.xlsx').sheet_by_index(1)
self_ = xlrd.open_workbook('/Users/zhangying/Desktop/哈哈哈.xlsx').sheet_by_index(0)
other = xlrd.open_workbook('/Users/zhangying/Desktop/哈哈哈.xlsx').sheet_by_index(1)

s = {}
o = {}
right_s = {}
right_o = {}
diff_s = {}
diff_o = {}
error_s = {}
error_o = {}

for i in range(self_.nrows):
    row_ = self_.row(i)
    try:
        key = str(int(row_[0].value))
    except:
        key = str(row_[0].value).strip()
    value = Decimal(row_[1].value).quantize(Decimal("0.000"))
    if key:
        if key in s:
            s[key].append(float(value))
        else:
            s[key] = []
            s[key].append(float(value))

for i in range(other.nrows):
    row_ = other.row(i)
    try:
        key = str(int(row_[0].value))
    except:
        key = str(row_[0].value).strip()

    value = Decimal(row_[1].value).quantize(Decimal("0.000"))
    if key:
        if key in o:
            o[key].append(float(value))
        else:
            o[key] = []
            o[key].append(float(value))
 
for k,v in s.items():
    total = Decimal(sum(v)).quantize(Decimal("0.000"))
    if k not in o:
        if k not in diff_s:
            diff_s[k] = []
            diff_s[k].extend(v)
        else:
            diff_s[k].extend(v)
        print(f"订单:{k}, 总价:{total}, 不再他方数据表中")
    else:
        anti_total = Decimal(sum(o[k])).quantize(Decimal("0.000"))
        if total != anti_total:
            print(f"订单:{k}, 不一致, 我方总价{total}, 他方{anti_total}")
            if k not in error_s:
                error_s[k] = []
                error_s[k].extend(v)
            else:
                error_s[k].extend(v)
        else:
            if k not in right_s:
                right_s[k] = []
                right_s[k].extend(v)
            else:
                right_s[k].extend(v)

print("---"*20)
for k,v in o.items():
    total_ = Decimal(sum(v)).quantize(Decimal("0.000"))
    if k not in s:
        if k not in diff_o:
            diff_o[k] = []
            diff_o[k].extend(v)
        else:
            diff_o[k].extend(v)
        print(f"订单:{k}, 总价:{total_}, 不再我方数据表中")
    else:
        anti_total_ = Decimal(sum(s[k])).quantize(Decimal("0.000"))
        if total_ != anti_total_:
            print(f"订单:{k}, 不一致, 他方总价{total_}, 我方{anti_total_}")
            if k not in error_o:
                error_o[k] = []
                error_o[k].extend(v)
            else:
                error_o[k].extend(v)
        else:
            if k not in right_o:
                right_o[k] = []
                right_o[k].extend(v)
            else:
                right_o[k].extend(v)

wb = xlwt.Workbook()
ws = wb.add_sheet('嘻嘻嘻')

style_error = xlwt.easyxf('pattern: pattern solid, fore_colour  yellow')
style_diff = xlwt.easyxf('pattern: pattern solid, fore_colour  orange')

sort_right_s = dict(sorted(right_s.items(), key=lambda item: item[0]))
sort_right_o = dict(sorted(right_o.items(), key=lambda item: item[0]))
sort_diff_s = dict(sorted(diff_s.items(), key=lambda item: item[0]))
sort_diff_o = dict(sorted(diff_o.items(), key=lambda item: item[0]))
sort_error_s = dict(sorted(error_s.items(), key=lambda item: item[0]))
sort_error_o = dict(sorted(error_o.items(), key=lambda item: item[0]))

row_end_1 = 0
row_end_2 = 0

error_diff = []
error_diff.extend(list(set(sort_error_s.keys()).difference(set(sort_error_o.keys()))))
error_diff.extend(list(set(sort_error_o.keys()).difference(set(sort_error_s.keys()))))

if len(sort_error_o) != len(sort_error_s) and error_diff:
    print("\n\n\n")
    print('###'*20)
    print('不一致的订单双方数量不一致，请注意!!!')
    print('###'*20)

for k,v in sort_error_s.items():
    for v_ in v:
        ws.write(row_end_1, 0, k,  style_error)
        ws.write(row_end_1, 1, v_, style_error)
        row_end_1 += 1

    if k in sort_error_o:
        for v__ in sort_error_o[k]:
            ws.write(row_end_2, 2, k, style_error)
            ws.write(row_end_2, 3, v__, style_error)
            row_end_2 += 1

    row_end_1 = row_end_2 = max(row_end_1, row_end_2)

for err_k in error_diff:
    if err_k in sort_error_s:
        for edv in sort_error_s[err_k]:
            ws.write(row_end_1, 0, err_k,  style_error)
            ws.write(row_end_1, 1, edv, style_error)
            row_end_1 += 1
            row_end_2 += 1

    if err_k in sort_error_o:
        for edv_ in sort_error_o[err_k]:
            ws.write(row_end_2, 2, err_k,  style_error)
            ws.write(row_end_2, 3, edv_, style_error)
            row_end_2 += 1

    row_end_1 = row_end_2 = max(row_end_1, row_end_2)

for k,v in sort_diff_s.items():
    for v_ in v:
        ws.write(row_end_1, 0, k, style_diff)
        ws.write(row_end_1, 1, v_, style_diff)
        row_end_1 += 1

    #  if k in sort_diff_o:
    #      for v__ in sort_diff_o[k]:
    #          ws.write(row_end_2, 2, k, style_diff)
    #          ws.write(row_end_2, 3, v__,style_diff)
    #          row_end_2 += 1

    row_end_1 = row_end_2 = max(row_end_1, row_end_2)

for k,v in sort_diff_o.items():
    for v_ in v:
        ws.write(row_end_1, 2, k, style_diff)
        ws.write(row_end_1, 3, v_, style_diff)
        row_end_1 += 1

    #  if k in sort_diff_s:
    #      for v__ in sort_diff_s[k]:
    #          ws.write(row_end_2, 2, k, style_diff)
    #          ws.write(row_end_2, 3, v__,style_diff)
    #          row_end_2 += 1
    row_end_1 = row_end_2 = max(row_end_1, row_end_2)

for k,v in sort_right_s.items():
    for v_ in v:
        ws.write(row_end_1, 0, k)
        ws.write(row_end_1, 1, v_)
        row_end_1 += 1

    if k in sort_right_o:
        for v__ in sort_right_o[k]:
            ws.write(row_end_2, 2, k)
            ws.write(row_end_2, 3, v__)
            row_end_2 += 1

    row_end_1 = row_end_2 = max(row_end_1, row_end_2)

# wb.save('c:\\Users\\zhangyunlong\\Desktop\\哈哈哈-1.xlsx')
wb.save('/Users/zhangying/Desktop/哈哈哈-1.xlsx')
print('\n\n')
input("文件生成完毕，按任意键退出")

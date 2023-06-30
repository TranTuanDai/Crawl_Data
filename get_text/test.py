import re
import pandas as pd
import io
# as per recommendation from @freylis, compile once only
CLEANR = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
html = """<ul>
	<li>Phản ứng phụ khi dùng thuốc hiếm khi xảy ra. Các phản ứng phụ thường gặp của Ibuprofen: rối loạn tiêu hóa như buồn nôn, nôn, khó tiêu, đau dạ dày, đau thượng vị, xuất huyết tiêu hóa, nhức đầu, chóng mặt. Paracetamol đôi khi có gây dị ứng, ban da, nôn, buồn nôn, một vài trường hợp có thể giảm toàn thể huyết cầu, giảm bạch cầu, thiếu máu, có thể gây suy gan (do hủy tế bào gan) khi dùng liều cao, kéo dài.</li>
	<li>Nguy cơ huyết khối tim mạch (xem thêm phần Thận trọng và cảnh báo đặc biệt khi sử dụng thuốc).</li>
	<li>Thông báo cho bác sĩ những tác dụng không mong muốn gặp phải khi sử dụng thuốc.</li>
</ul>"""
def cleanhtml(raw_html):
  cleantext = re.sub(CLEANR, '', raw_html)
  return cleantext
result = cleanhtml(html)
df = pd.read_csv(io.StringIO(result), sep=";", header = None)

print(df)
print(result)



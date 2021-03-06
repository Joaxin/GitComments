# 1. 加上了solid_capstyle = 'butt'这个参数，去掉了直线的‘帽子’
#
# 2.设置antialiased=False， 取消直线边缘模糊化处理
#
# 3.每段序列左右两端加了0.5

def find_target_data(gene_name, gtf_file_path, chunk=3072 * 2048):
    with open(gtf_file_path) as f:
        header = ['chr', 'db', 'record', 'start', 'end', 'tmp', 'strand', 'tmp', 'info']
        target_data = {}
        get = 0
        buffer_list = ['']
        print('Please wait for 10 seconds: ')
        while True:
            buffer = buffer_list[-1] + f.read(chunk)
            print((buffer[buffer.find('\n') + 1:buffer.find('\n') + 3]), end='\r')
            if ('gene_name "' + gene_name.upper() + '"') in buffer:
                buffer_list = buffer.split('\n')
                for line in buffer_list[:-1]:
                    if ('gene_name "' + gene_name.upper() + '"') in line:
                        get = 1
                        line_list = line.split('\t')
                        for i in range(len(line_list)):
                            try:
                                target_data[header[i]].append(line_list[i])
                            except:
                                target_data[header[i]] = [line_list[i]]
            else:
                if get == 1:
                    break
            if len(buffer) < chunk:
                break
        if not target_data:
            print('\n\n There is some wrong with your gene name!\n')
            raise NameError('your gene_name is not exit')
        print("\nHave got the gene information!")
    return (target_data)


def draw_gene_structure(gene_name, target_data, png_path='', line_width=5):
    gene_symbol = gene_name.upper()
    if not png_path:
        png_path = gene_symbol + '.png'
    # 定义颜色的字典
    tmp_colors = ['lime', 'red', 'blue', 'yellow', 'yellow', 'w']
    names_tmp_colors = ['gene', 'CDS', 'exon', 'three_prime_utr', 'five_prime_utr', 'stop_codon']
    colors_legend_name = ['gene', 'CDS_exon', 'non_CDS_exon', 'UTR_exon']
    color_dict = dict(zip(names_tmp_colors, tmp_colors))

    # 提取转录本名称
    import re
    transcript_list = []
    for i in target_data['info']:
        try:
            transcript_name = re.findall('transcript_name "(.*?)"', i)[0]
            if transcript_name not in transcript_list:
                transcript_list.append(transcript_name)
        except:
            pass
    # 计算转录本数目
    transcript_num = 0
    for i in target_data['record']:
        if i == 'transcript':
            transcript_num += 1

    import numpy as np
    import matplotlib.patches as mpatches
    import matplotlib.pyplot as plt
    import matplotlib.lines as lines
    fig = plt.figure(1)
    # 设置不透明度，默认为1
    fig.patch.set_alpha(1)
    fig.patch.set_facecolor('w')
    num = 0  # 当前转录本数目标志
    warnings = []
    for i in range(len(target_data['record'])):
        if target_data['record'][i] == 'gene':
            # 判断正反链
            if target_data['strand'][i] == '+':
                arr = '->'
            else:
                arr = '<-'
            # 图的第一个区域
            # add_axes 是在一张图上指定特定区域作图，第一个数字为从左边%20处，下面20%处开始，宽50%，高60%区域作图
            ax = fig.add_axes([0.2, 0.2, 0.5, 0.6])
            # 定义基因方向箭头
            arrow = mpatches.FancyArrowPatch(
                (int(target_data['start'][i]), 0.1),
                (int(target_data['end'][i]), 0.1),
                arrowstyle=arr,
                mutation_scale=25, lw=1, color='lime', antialiased=True)  # antialiased默认为True，边缘平滑处理
            # 画箭头
            ax.add_patch(arrow)
            # 坐标轴标签
            ax.set_xlim([int(target_data['start'][i]), int(target_data['end'][i])])
            ax.set_ylim([-0.5, transcript_num + 1])
            ax.set_xticks(np.linspace(int(target_data['start'][i]), int(target_data['end'][i]), 5))
            ax.set_yticks([0.1] + list(range(1, transcript_num + 1)))
            ax.set_yticklabels(['gene'] + transcript_list)
            ax.set_xticklabels(
                [int(i) for i in np.linspace(int(target_data['start'][i]), int(target_data['end'][i]), 5)])
            # 坐标轴显示
            ax.spines['top'].set_visible(False)
            ax.spines['left'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.get_xaxis().tick_bottom()
            ax.get_yaxis().tick_left()
            ax.get_xaxis().set_tick_params(direction='out')
            ax.tick_params(axis=u'y', which=u'both', length=0)
            # 坐标轴字体大小
            for tick in ax.xaxis.get_major_ticks():
                tick.label.set_fontsize(6)
            for tick in ax.yaxis.get_major_ticks():
                tick.label.set_fontsize(6)
        elif target_data['record'][i] == 'transcript':
            num += 1  # 转录本所有区域计数作图
            line1 = [(int(target_data['start'][i]), num), (int(target_data['end'][i]), num)]
            (line1_xs, line1_ys) = zip(*line1)
            ax.add_line(lines.Line2D(line1_xs, line1_ys, linewidth=0.2,
                                     solid_capstyle='butt', solid_joinstyle='miter',
                                     antialiased=False, color='black'))
        elif target_data['record'][i] in color_dict.keys():
            # 添加结构图
            line2 = [(int(target_data['start'][i]) - 0.5, num), (int(target_data['end'][i]) + 0.5, num)]
            (line2_xs, line2_ys) = zip(*line2)
            ax.add_line(lines.Line2D(line2_xs, line2_ys,
                                     solid_capstyle='butt', solid_joinstyle='miter',
                                     linewidth=int(line_width), alpha=1,
                                     color=color_dict[target_data['record'][i]],
                                     antialiased=False))
        else:
            warnings.append(target_data['record'][i])
    if warnings:
        print('\nTips: ')
        print(' and '.join([i for i in set(warnings)]) + ' is not in our consideration!!!!!!')

    # 做图例
    # add_axes 是在一张图上指定特定区域作图，第一个数字为从左边%74处，下面20%处开始，宽20%，高60%区域作图
    ax_legend = fig.add_axes([0.76, 0.2, 0.2, 0.6])
    # ax_legend.set_xticks([])
    # ax_legend.set_yticks([])
    for i in range(len(colors_legend_name)):
        line3 = [(0, (9 - i) * 0.1), (0.1, (9 - i) * 0.1)]
        (line3_xs, line3_ys) = zip(*line3)
        ax_legend.add_line(lines.Line2D(line3_xs, line3_ys, linewidth=5,
                                        color=color_dict[names_tmp_colors[i]],
                                        solid_capstyle='butt', solid_joinstyle='miter',
                                        antialiased=False))
        ax_legend.text(0.2, (8.9 - i) * 0.1, colors_legend_name[i], fontsize=6)
    ax_legend.set_axis_off()
    # 加标题
    fig.suptitle('\n\n\nchr' + str(target_data['chr'][0]) + ': ' + gene_symbol, fontsize=10)
    # 保存图片
    fig.savefig(png_path, dpi=150)
    plt.show()
    print('\nThe picture file is completed: ' + png_path)
    print("All transcripts of " + gene_name + ':\n' + " ".join(sorted(transcript_list)))
    return (png_path)


# gtf文件下载地址：
# [url]ftp://ftp.ensembl.org/pub/release-87/gtf/homo_sapiens/Homo_sapiens.GRCh38.87.chr.gtf.gz[/url]
gtf_file_path = 'Homo_sapiens.GRCh38.87.chr.gtf'

gene_name = input('Please enter the gene_name: ').strip()
line_width = input('Please enter the line_width: ').strip()

if not line_width:
    line_width = 5
if not gene_name:
    gene_name = input('Please enter the gene_name: ').strip()
else:
    gene_name = 'TP53'
    # gene_name = 'hoxc8'
    # gene_name = 'AnXA1'

# 计算消耗时间
import time

start = time.time()

# 提取目标基因的数据
target_data = find_target_data(gene_name=gene_name, gtf_file_path=gtf_file_path)
# 作图
draw_gene_structure(gene_name, target_data, line_width=line_width)

print('\n used %.2f s to get the target information and get its structure!' % (time.time() - start))
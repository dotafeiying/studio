#-*- coding: utf-8 -*-
import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "studio.settings")
django.setup()

from app.models import Article,Category,Type,About,AboutType


def main():
    columns_urls = [
        ('国考', 'sk'),
        ('省考', 'gk'),
        ('选调生', 'xds'),
        ('事业单位','sy'),
        ('教师招考','js'),
        ('大学生村官','cg'),
        ('三支一扶','szyf')
    ]
    columns_urls1=[
        ('真题','zt'),
        ('招考资讯','zx'),
        ('面试锦囊','ms'),
        ('辅导简章','jz')
    ]
    columns_urls2 = [
        ('关于我们', 'us'),
        ('加入我们', 'join'),
        ('名师简介', 'ms'),
        ('员工生活', 'life')
    ]
    for column_name, url in columns_urls2:
        c=AboutType.objects.get_or_create(name=column_name,slug=url)[0]

    for column_name, url in columns_urls:
        for column_name1, url1 in columns_urls1:
            c = Category.objects.get_or_create(name=column_name, slug=url)[0]
            t= Type.objects.get_or_create(name=column_name1, slug=url1)[0]

            # 创建 10 篇新闻
            for i in range(1, 11):
                article = Article.objects.get_or_create(
                    title='湖北省武汉市标题一定要长{}_{}_{}'.format(column_name, column_name1, i),
                    # slug='article_{}'.format(i),
                    status='p',
                    body='''新闻详细内容： {} {} {}参加体检须携带本人身份证、笔试准考证、毕业证和学位证的原件、复印件.根据《武汉市2017年度事业单位面向社会公开招聘工作人员实施方案》，经笔试、人机对话、集中面试、体检、考核等程序，部分单位招聘工作现已结束。现将江岸区2017年事业单位公开招聘拟聘用人员(非教育系统第一批)进行公示。公示期间，如有异议，可向江岸区人力资源局反映。
                        公示时间：2017年7月26日至2017年8月3日。
                        江岸区人力资源局监督电话：027-82717795。
                        原标题：2017年度江岸区事业单位公开招聘拟聘用人员公示(非教育系统第一批)
                        点击下载>>>
                        2017年江岸区事业单位公开招聘拟聘用人员公示表.xls
                        '''.format(column_name,column_name1, i),
                    category=c,
                    type=t
                )[0]
                # article.category.add
                # article.column.add(c)



if __name__ == '__main__':
    main()
    print("Done!")
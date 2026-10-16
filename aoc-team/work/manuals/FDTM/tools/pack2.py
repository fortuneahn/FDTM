import sys,json,hashlib,shutil,os,zipfile,difflib,re
sys.path.insert(0,r'C:\Users\안상준\AppData\Local\Temp\claude\C--Users-----Desktop-KCNAIR------\c9d37257-c1eb-4178-9366-292b1961c11f\scratchpad\edit')
from lib import PAT,ptext
ROOT=r'C:\Users\안상준\Desktop\KCNAIR\교범작성팀\aoc-team'
SC=r'C:\Users\안상준\AppData\Local\Temp\claude\C--Users-----Desktop-KCNAIR------\c9d37257-c1eb-4178-9366-292b1961c11f\scratchpad'
SRC=r'C:\Users\안상준\Desktop\규정\운항관리사훈련교범(FDTM)\FDTM_Rev02_개정안.docx'
W=os.path.join(ROOT,'work','manuals','FDTM')
NEW=os.path.join(W,'FDTM_Rev02_수정안.docx')
def paras(path):
    x=zipfile.ZipFile(path).read('word/document.xml').decode('utf8')
    return [ptext(m.group(0)) for m in PAT.finditer(x)]
A=paras(SRC); B=paras(NEW)
log=json.load(open(os.path.join(SC,'edit','log.json'),encoding='utf8'))
why={}
for L,k,o,n,w in log:
    if L and w: why.setdefault(L,[]).append(w)
whynew={n:w for L,k,o,n,w in log if n}
POLICY=('라. 훈련 실시 결과와','마. 외부 전문가 특례','다. 실무자격심사 — 불합격 시','나. 유예 —','나. 실시 — 정기훈련 6.18')
ia=[i for i,t in enumerate(A) if t.strip()]; ib=[j for j,t in enumerate(B) if t.strip()]
a=[A[i] for i in ia]; b=[B[j] for j in ib]
sm=difflib.SequenceMatcher(None,a,b,autojunk=False)
rows=[]
def c(s): return (s or '').replace('|','\\|').replace('\n',' ')
deleted=set(); ops=sm.get_opcodes()
for tag,i1,i2,j1,j2 in ops:
    if tag in('delete','replace'): deleted.update(a[i1:i2])
for tag,i1,i2,j1,j2 in ops:
    if tag=='equal': continue
    n=max(i2-i1,j2-j1)
    for k in range(n):
        o=a[i1+k] if i1+k<i2 else ''
        nw=b[j1+k] if j1+k<j2 else ''
        L=ia[i1+k]+1 if o else None
        if o and nw: kind='수정'
        elif o: kind='삭제'
        else: kind='신설'
        if nw and not o and nw in deleted: kind='이동(위치 변경)'
        w='; '.join(dict.fromkeys(why.get(L,[]))) if L else whynew.get(nw,'')
        if not w: w=whynew.get(nw,'')
        if nw.startswith(POLICY): kind+=' ※회사 정책 신설·사람 승인 필요'
        rows.append((L or '-',kind,o,nw,w))
# 삭제된 문장이 다른 위치로 이동한 경우 표기
bset=set(b)
rows2=[]
for L,k,o,nw,w in rows:
    if k=='삭제' and o in bset: k='삭제(다른 위치로 이동, 이동 행 참조)'
    rows2.append((L,k,o,nw,w))
cnt={}
for r in rows2: cnt[r[1].split(' ')[0]]=cnt.get(r[1].split(' ')[0],0)+1
lines=['# FDTM Rev.02 수정안 신·구 대비표 (원본→수정안 1:1)','','작업 ID: TASK-FDTM-REV02-001 (3차 스냅샷)','기준 원본: FDTM_Rev02_개정안.docx','수정본: FDTM_Rev02_수정안.docx (변경 단락 좌측 적색 개정 바)','작성 방식: 원본과 수정본 단락을 자동 비교해 생성(중간 상태 행 없음). 원본 단락 번호는 문서 본문 순서(빈 단락 포함)다.','','구분별 건수: '+', '.join('%s %d'%(k,v) for k,v in cnt.items())+' (총 %d행)'%len(rows2),'','| # | 원본 단락 번호 | 구분 | 구 | 신 | 사유 |','|---|---|---|---|---|---|']
for n,(L,k,o,nw,w) in enumerate(rows2,1):
    lines.append('| %d | %s | %s | %s | %s | %s |'%(n,L,k,c(o),c(nw),c(w)))
tx='\n'.join(lines)+'\n'
open(os.path.join(W,'FDTM_Rev02_신구대비표.md'),'w',encoding='utf8').write(tx)
I=os.path.join(ROOT,'work','integrated','TASK-FDTM-REV02-001-r3'); os.makedirs(I,exist_ok=True)
man=['# 통합 스냅샷 r3','','작업 ID: TASK-FDTM-REV02-001','revision: FDTM Rev.02 수정안 3차 (DRAFT, 미인가·미발효, 기계적 정리 반영)','생성일: 2026-10-16','','| 파일 | SHA256 |','|---|---|']
for f in ('FDTM_Rev02_수정안.docx','FDTM_Rev02_수정안.pdf','FDTM_Rev02_신구대비표.md'):
    shutil.copy(os.path.join(W,f),os.path.join(I,f))
    man.append('| %s | %s |'%(f,hashlib.sha256(open(os.path.join(I,f),'rb').read()).hexdigest()))
open(os.path.join(I,'MANIFEST.md'),'w',encoding='utf8').write('\n'.join(man)+'\n')
print(cnt,len(rows2))

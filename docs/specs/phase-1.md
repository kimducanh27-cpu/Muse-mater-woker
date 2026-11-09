# PHASE 1 — ZERO-CODE ARCHITECTURE & DESIGN SPECS

> Converted from the supplied PDF. Source wording and sequence are retained; PDF page markers and extraction-only placeholders are omitted.

## PHASE 1 SPEC: ZERO-CODE ARCHITECTURE &
## DESIGN SPECS
Agent Execution Specification & Full Copy-Paste Prompt Suite for Zero-Code Design
Systems, W3C DTCG Tokens, and Component Contracts.

## 1. CORE INVARIANTS (HARD RULES)
1. Zero-Code Boundary: Tuyệt đối không sinh mã nguồn JSX, TSX, CSS, hoặc Compose
trong Phiên 1. Toàn bộ đầu ra là file đặc tả (.md, .json, .yaml).
2. Standard Conformance:
  - Token phải tuân thủ 100% định dạng W3C Design Tokens Community Group
(DTCG) với hai khóa bắt buộc $value và $type.
  - Component contracts bắt buộc tuân theo lược đồ sherizan/design-model.
  - File SSOT tổng hợp bắt buộc tuân theo cấu trúc
google-labs-code/design.md.
3. No Made-up Values: Giá trị primitive tokens (màu sắc, bước thang 50-950) phải được
trích xuất từ các hệ thống thiết kế mở đã được kiểm chứng (primer/primitives hoặc
adobe/spectrum-tokens), không tự ý bịa mã màu HEX tùy hứng.
4. Mathematical Accessibility: 100% cặp màu ngữ nghĩa tương tác (text/icon trên
background) phải đạt chuẩn tương phản toán học WCAG 2.1 AA (contrast ratio >= 4.5:1
cho text thông thường, >= 3.0:1 cho text lớn/UI components).
5. Single Source of Truth (SSOT): DESIGN.md là tài liệu duy nhất tích hợp toàn bộ token
schema, component contracts và design rationale.
6. One-Way Freeze Gate: Khi Phiên 1 kết thúc và bàn giao, toàn bộ tài sản được đóng
băng (freeze). Phiên 2 chỉ có quyền đọc; cấm Agent 2 tự ý sửa ngược spec. Nếu thiếu
token hoặc sai logic, Agent 2 bắt buộc phải báo lỗi "Spec Drift" và xin ý kiến thay vì tự
sửa.

2. Pre-Flight Check & Workspace Setup

#### 2.0. Danh mục Standards & GitHub Repositories tham chiếu
- Primitive Tokens Source: primer/primitives (GitHub) hoặc
adobe/spectrum-tokens (Adobe)
- Token Format Specification: W3C Design Tokens Community Group
(design-tokens/community-group)
- Component Modeling Specification: sherizan/design-model
- Design System SSOT Standard: google-labs-code/design.md
- Accessibility Standard: W3C Web Content Accessibility Guidelines (WCAG) 2.1 Level
## AA

#### 2.1. Directory Structure Blueprint

File / Path                        Vai trò & Mục đích                  Định dạng chuẩn

Brand identity, visual density,
docs/PRODUCT.md                                                        Markdown
visual tone, moodboard

Ràng buộc kỹ thuật, nền tảng
docs/charter.md                                                        Markdown
đích, tiêu chuẩn WCAG

tokens/primitives.tokens.j         Giá trị màu thô 50-950, lưới 4px
## W3C DTCG JSON
son                                spacing, radius, shadow

tokens/semantics.light.tok         Danh mục ánh xạ token ngữ
## W3C DTCG JSON
ens.json                           nghĩa cho Light Mode

tokens/semantics.dark.toke         Danh mục ánh xạ token ngữ
## W3C DTCG JSON
ns.json                            nghĩa cho Dark Mode

models/components.model.ya         Hợp đồng linh kiện, ma trận trạng
Design-Model YAML
ml                                 thái, platform mapping

Single Source of Truth tổng hợp
DESIGN.md                                                              Markdown + YAML Frontma…
## (SSOT)

Báo cáo kiểm định toán học
docs/audit-report.md                                                   Markdown
## WCAG 2.1 AA

#### 2.2. Automated Workspace Bootstrap Script
File script scripts/bootstrap-phase1.sh để khởi tạo cấu trúc thư mục và file trắng:

Shell‎
#!/usr/bin/env bash
set -euo pipefail

echo "=== Khởi tạo workspace Phiên 1 (Zero-Code Architecture) ==="
mkdir -p docs tokens models scripts

touch docs/PRODUCT.md
touch docs/charter.md
touch tokens/primitives.tokens.json
touch tokens/semantics.light.tokens.json

touch tokens/semantics.dark.tokens.json
touch models/components.model.yaml
touch DESIGN.md

echo "[PASS] Khởi tạo thư mục và template files thành công."

2. 3. Prompt: Pre-flight Audit & Diagnostic

None‎
Thực hiện PRE-FLIGHT CHECK toàn bộ môi trường trước khi khởi chạy Phiên 1:

## 1. KIỂM TRA WORKSPACE & DIRECTORIES:
- Xác minh sự tồn tại của các thư mục: `docs/`, `tokens/`, `models/`.
- Xác nhận các file: `docs/PRODUCT.md`, `tokens/primitives.tokens.json`,
`tokens/semantics.light.tokens.json`, `tokens/semantics.dark.tokens.json`,
`models/components.model.yaml`, và `DESIGN.md` đã sẵn sàng nhận ghi dữ liệu.

## 2. KIỂM TRA AGENT SKILLS:
- Xác nhận khả năng nhận diện và thực thi các slash commands:
/impeccable-init, /grilling, /impeccable-typeset, /impeccable-colorize,
/impeccable-shape, /impeccable-audit.

## 3. KIỂM TRA THÔNG TIN ĐẦU VÀO:
- Xác nhận người dùng đã có định hướng sản phẩm, đối tượng sử dụng và nền
tảng đích (Web / Mobile Android).

## ĐẦU RA:
In ra bảng chẩn đoán:
| Hạng mục | Trạng thái (PASS / FAIL / MISSING) | Chi tiết |
Nếu có mục FAIL/MISSING, tự động chạy script bootstrap hoặc yêu cầu bổ sung
thông tin.

2. 4. Prompt: Auto-Bootstrap & Workspace Init

None‎
Dựa trên bảng Pre-flight Check vừa thực hiện:

Hãy tự động thực hiện các hành động sau để đưa hệ thống về trạng thái PASS:

1. Tạo cấu trúc thư mục cần thiết:
mkdir -p docs tokens models scripts
2. Khởi tạo sẵn các file trắng:
touch docs/PRODUCT.md docs/charter.md tokens/primitives.tokens.json
tokens/semantics.light.tokens.json tokens/semantics.dark.tokens.json
models/components.model.yaml DESIGN.md
3. Cấp quyền thực thi và xác nhận: [READY FOR STEP 1].

## 3. SIX-STEP EXECUTION PIPELINE & FULL PROMPTS

### Step 0: Session Setup

None‎
Bạn đóng vai trò Design Systems Architect trong Phiên 1 (Zero-Code Architecture
& Design Specs).
Nhiệm vụ: Thiết lập toàn bộ quy chuẩn thiết kế, bảng W3C DTCG tokens (tách
riêng light/dark), component contracts có platform mapping và đóng gói
DESIGN.md.

## RÀNG BUỘC CỐT LÕI:
1. ZERO-CODE: Tuyệt đối không sinh mã nguồn JSX, TSX, CSS, hoặc Compose.
2. Tuân thủ định dạng W3C DTCG ($value, $type) cho tokens. Tách rõ 2 file:
`tokens/semantics.light.tokens.json` và `tokens/semantics.dark.tokens.json`.
3. Kế thừa bảng màu từ @primer/primitives hoặc @adobe/spectrum-tokens, không tự
chế mã màu HEX.
#### 4. Đảm bảo 100% cặp màu tương tác đạt WCAG 2.1 AA (tương phản >= 4.5:1).
5. Khóa component contracts theo chuẩn sherizan/design-model và bắt buộc có
block `platform_mapping` cho Web và Android.
6. One-Way Freeze: Tài sản sau khi hoàn tất sẽ được đóng băng cho Phiên 2.

Xác nhận đã hiểu và sẵn sàng nhận lệnh Step 1.

### Step 1: Dual-Track Discovery

#### Prompt 1.1: Brand Discovery qua /impeccable-init

None‎
/impeccable-init
Hãy tiến hành phỏng vấn ngắn gọn để xác lập nền tảng thương hiệu và thẩm mỹ cho
dự án:

1. Xác định Brand Voice và tính cách sản phẩm (ví dụ: tối giản, hiện đại, công
nghệ, thân thiện).
2. Định hình Visual Density (mật độ hiển thị: compact, comfortable, loose).
#### 3. Đề xuất bảng moodboard và nguyên tắc thị giác cốt lõi.

## ĐẦU RA:
Ghi kết quả vào file `docs/PRODUCT.md` theo cấu trúc chuẩn: Brand Principles,
Visual Tone, Typography Mood, Elevation & Radius Direction.

#### Prompt 1.2: Technical & Constraint Discovery qua /grilling

None‎
/grilling
Chất vấn và khóa các ràng buộc kỹ thuật cốt lõi của Design System:
1. Nền tảng đích: Web (Next.js / Tailwind CSS) và Mobile (Android / Jetpack
Compose).
2. Chuẩn tiếp cận: WCAG 2.1 Level AA bắt buộc.
3. Chế độ màu: Hỗ trợ song song Light Mode và Dark Mode.
4. Viewport quy chuẩn: Mobile (375px) và Desktop (1440px).

## ĐẦU RA:
Consolidate all technical architecture decisions into `docs/charter.md`.

### Step 2: Primitive Tokens Construction (W3C DTCG)

None‎
Đọc @docs/PRODUCT.md và @docs/charter.md:
Hãy trích xuất và khởi tạo bảng Primitive Tokens theo chuẩn W3C DTCG ($value và
$type):

1. Color Scale: Kế thừa bảng màu bậc thang 50-950 từ @primer/primitives hoặc
@adobe/spectrum-tokens cho các dải màu (Neutral, Primary/Brand, Success,
Warning, Danger, Info).
2. Spacing Scale: Khóa lưới 4px cơ sở (4, 8, 12, 16, 24, 32, 48, 64px).
3. Border Radius Scale: none (0px), sm (4px), md (8px), lg (12px), full
(9999px).
4. Elevation / Shadow Scale: 4 cấp độ (elevation.1 đến elevation.4).

## ĐẦU RA:
Ghi toàn bộ định nghĩa vào file `tokens/primitives.tokens.json`.
RÀNG BUỘC: Định dạng JSON 100% hợp lệ, có $value và $type. Không viết mã CSS.

### Step 3: Semantic Tokens Mapping (Typography & Light/Dark Mode)

#### Prompt 3.1: Typography Scale qua /impeccable-typeset

None‎
/impeccable-typeset
Đọc @tokens/primitives.tokens.json:
Tính toán thang bậc kiểu chữ (Typography Scale) dựa trên Modular Scale tỷ lệ
### 1.25 (Major Third):
1. Định nghĩa các cấp bậc: Display, Heading 1, Heading 2, Heading 3, Body
Large, Body Regular, Caption.
2. Với mỗi cấp bậc, chỉ rõ: font-size, line-height (bội số lưới 4px),
font-weight, letter-spacing.
### 3. Định nghĩa Font Family (System font stack cho Web và Roboto/Inter cho
Android).

## ĐẦU RA:
Ghi cấu trúc typography tokens vào cả 2 file
`tokens/semantics.light.tokens.json` và `tokens/semantics.dark.tokens.json`.

#### Prompt 3.2: Color Semantics Mapping qua /impeccable-colorize (Tách riêng
Light & Dark)

None‎
/impeccable-colorize
Đọc @tokens/primitives.tokens.json và @docs/charter.md:
Thiết lập danh mục Semantic Color Tokens, tách biệt thành 2 file có cùng
key-name 100% nhưng khác target alias:

#### 1. `tokens/semantics.light.tokens.json`:
- surface: canvas, subtle, raised, overlay (ánh xạ dải sáng).
- text: primary, secondary, muted, inverse, brand.
- border: default, subtle, strong, focus.
- action: primary.default, primary.hover, primary.active, primary.disabled.
- feedback: success, warning, danger, info.

#### 2. `tokens/semantics.dark.tokens.json`:
- Cùng 100% danh mục key như trên, nhưng ánh xạ sang dải màu tối từ
primitives để đảm bảo tương phản WCAG trong Dark Mode.

## ĐẦU RA:

Lưu thành 2 file JSON riêng biệt: `tokens/semantics.light.tokens.json` và
`tokens/semantics.dark.tokens.json`. 100% giá trị là alias
`{color.primitive...}`.

### Step 4: Component Contracts Modeling (sherizan/design-model)

None‎
/impeccable-shape
Đọc @tokens/semantics.light.tokens.json, @tokens/semantics.dark.tokens.json và
@docs/PRODUCT.md:
Hãy mô hình hóa hợp đồng linh kiện (Component Contract) cho các linh kiện nền
tảng (ví dụ Button, Input, Modal) theo chuẩn sherizan/design-model:

1. Metadata & Props:
- Tên linh kiện, mô tả chức năng.
- Props: variants (primary, secondary, destructive), sizes (sm, md, lg),
states.
- Slots: leading-icon, label, trailing-icon.
2. State Matrix:
- Default, Hover, Active, Focus, Disabled, Loading, Error.
- Ánh xạ rõ token semantic cho từng trạng thái.
3. Platform Mapping (RÀNG BUỘC BẮT BUỘC):
- Khai báo mapping cờ logic cho từng nền tảng:
platform_mapping:
web:
disabled: "disabled"
loading: "aria-busy"
android:
disabled: "!enabled"
loading: "isLoading"
4. UX Constraints:
- Touch target: tối thiểu 44x44px trên touch viewport.
- Text constraints: truncate hoặc safe wrap cho nhãn dài.
- Business rules: Tối đa 1 Primary Action trong cùng một view/action group.

## ĐẦU RA:
Lưu vào file `models/components.model.yaml` định dạng YAML chuẩn.

None‎
/impeccable-audit
Đọc @tokens/primitives.tokens.json, @tokens/semantics.light.tokens.json,
@tokens/semantics.dark.tokens.json, và @models/components.model.yaml:

## 1. KIỂM ĐỊNH TOÁN HỌC WCAG 2.1 AA:
- Tính toán tỷ lệ tương phản cho toàn bộ cặp màu text/surface trong cả Light
Mode và Dark Mode.
- Đảm bảo contrast ratio >= 4.5:1 (text thông thường) và >= 3.0:1 (text lớn,
borders, icons).
- Quét lỗi broken alias hoặc token mồ côi.

## 2. ĐÓNG GÓI SSOT DESIGN.MD:
- Khởi tạo file `DESIGN.md` theo chuẩn google-labs-code/design.md.
- YAML Frontmatter: Khai báo toàn bộ token schema (cả light và dark),
typography scale, component metadata và platform mapping.
- Markdown Body: Ghi nhận rationale, bảng tra cứu màu sắc 2 mode, hướng dẫn
tích hợp và kết quả audit.

## ĐẦU RA:
1. Ghi file `DESIGN.md`.
2. Xuất báo cáo kiểm định vào `docs/audit-report.md`.

### Step 6: Handoff Gate & Asset Freeze (One-Way Freeze)

None‎
Rà soát toàn bộ tài sản bàn giao trước khi đóng Phiên 1:
1. Kiểm tra tính toàn vẹn của:
- `DESIGN.md`
- `docs/PRODUCT.md`
- `docs/charter.md`
- `docs/audit-report.md`
- `tokens/primitives.tokens.json`
- `tokens/semantics.light.tokens.json`
- `tokens/semantics.dark.tokens.json`
- `models/components.model.yaml` (có đủ platform_mapping)
#### 2. Đảm bảo không có bất kỳ file code (.tsx, .jsx, .css, .kt) nào được sinh ra
ngoài ý muốn.
3. Thực hiện commit Git để đóng băng tài sản (One-Way Freeze):
git add DESIGN.md docs/ tokens/ models/
git commit -m "chore(design-system): freeze zero-code tokens, contracts and
DESIGN.md"
4. Thiết lập quy tắc cho Phiên 2: Spec đã đóng băng là Read-Only. Bất kỳ sự sai
lệch nào cũng phải dừng lại báo cáo lỗi "Spec Drift".
5. Thông báo: [PHASE 1 COMPLETE - READY FOR PHASE 2 IMPLEMENTATION].

## 4. BẢNG TIÊU CHÍ NGHIỆM THU (EXIT CRITERIA & COMPLIANCE
## MATRIX)

Hạng mục kiểm tra        Tiêu chuẩn bắt buộc                 Phương pháp xác minh

100% W3C DTCG format ($value,       Automated JSON schema
Token Specification
$type), tách rõ file Light & Dark   validator

### 0 mã màu tự chế; 100% ánh xạ từ
Primitive Provenance     @primer/primitives hoặc             Audit đối chiếu primitive mapping
@adobe/spectrum-tokens

100% cặp màu tương tác >= 4.5:1
Mathematical contrast log trong
Accessibility Standard   contrast trong cả Light và Dark
docs/audit-report.md
mode

Đầy đủ State Matrix, UX
Schema validation của
Component Contracts      constraints và block
models/components.model.yaml
`platform_mapping`

Đầy đủ metadata frontmatter và
SSOT Integration                                             Structure check trên DESIGN.md
documentation body

### 0 file mã nguồn thực thi (.jsx,
Zero-Code Policy                                             File extension scan
.tsx, .css, .kt)

Tài sản được đóng băng qua Git
One-Way Freeze           commit, spec trở thành              Git commit log check
Read-Only

# PHASE 2 — PRODUCTION CODE & VISUAL CLOSED-LOOP

> Converted from the supplied PDF. Source wording and sequence are retained; PDF page markers and extraction-only placeholders are omitted.

## PHASE 2 SPEC: PRODUCTION CODE & VISUAL
## CLOSED-LOOP
Agent Execution Specification & Full Copy-Paste Prompt Suite for Web &
Android Design System Components.

## 1. INVARIANTS (HARD RULES)
1. Single Source of Truth (SSOT): Mọi style và component structure bắt buộc đọc từ
@DESIGN.md, @tokens/semantics.light.tokens.json,
@tokens/semantics.dark.tokens.json, và @models/components.model.yaml.
2. Zero Hardcoded Values:
  - Cấm mã màu Hex thô: #[0-9a-fA-F]{3,8}.
  - Cấm số pixel/dp tùy tiện ngoài lưới 4px.
  - 100% màu sắc và kích thước phải map qua semantic tokens.
3. Contract Boundary: Chỉ implement đúng các variants, sizes, slots và states có trong
contract. Cấm tự ý thêm props hoặc variants ngoài spec. Bám sát platform_mapping.
4. Visual Loop Gate: Component chỉ được coi là hoàn tất khi đã kết xuất ảnh snapshot
thực tế (Playwright / Paparazzi) và vượt qua bước kiểm định Vision.
5. One-Way Freeze Gate: Toàn bộ tài sản từ Phiên 1 là Read-Only. Agent 2 tuyệt đối không
được tự ý sửa ngược file DESIGN.md hay models/components.model.yaml. Nếu phát
hiện thiếu token hoặc sai logic, Agent 2 bắt buộc phải dừng lại và báo lỗi "Spec Drift".
6. Dual Sub-Agent Audit & Veto Rule (EGM Protocol):
  - Agent chính cấm tự đánh giá thẩm mỹ và chất lượng code của chính mình.
  - Bắt buộc dispatch song song 2 Sub-agent độc lập với ngữ cảnh cô lập (Fresh
Context):
    - Sub-agent 1 (Vision & UX Auditor): Soi ảnh snapshot PNG +
@DESIGN.md qua /impeccable critique.
    - Sub-agent 2 (Spec & Code Auditor): Soi Git Diff +
@models/components.model.yaml qua /code-review.
  - Strict Read-Only Auditor Rule: Cả 2 Sub-agent chỉ thẩm định và xuất
Deficiency Report; nghiêm cấm tự ý sửa code.
  - Luật phủ quyết (Veto Rule): Chỉ cần 1 sub-agent REJECT, Agent chính bắt buộc
phải sửa lỗi (ngân sách tối đa 3 vòng lặp). Chỉ commit khi cả 2 cùng PASS.

## 2. PRE-FLIGHT CHECK & AUTO-BOOTSTRAP
Xác minh sự tồn tại của 6 tài sản cốt lõi trước khi bắt đầu:

#### 2.0. Danh mục GitHub Repositories tham chiếu (Official Reference Repos)
- Web Preview: ladle-dev/ladle
- Web Visual Test: microsoft/playwright
- Web Linter: schoero/eslint-plugin-tailwindcss (rule no-arbitrary-value),
AndyOGo/stylelint-declaration-strict-value
- Android Snapshot: cashapp/paparazzi (plugin app.cash.paparazzi)
- Android Preview Catalog: airbnb/Showkase (com.airbnb.android:showkase)
- Android Linter: slackhq/compose-lints

#### 2.1. File Verification Checklist
- @DESIGN.md (YAML frontmatter + token schema)
- @tokens/primitives.tokens.json (W3C DTCG format: $value, $type)
- @tokens/semantics.light.tokens.json (Light mode aliases)
- @tokens/semantics.dark.tokens.json (Dark mode aliases)
- @models/components.model.yaml (contracts, states, platform_mapping)
- @docs/PRODUCT.md (brand context & principles)

#### 2.2. Automated Workspace Bootstrap Script
File script scripts/lint-tokens.sh dùng để chặn hardcode:

Shell‎
#!/usr/bin/env bash
set -euo pipefail
TARGET="${1:-src}"
MATCHES=$(grep -rnE "#[0-9a-fA-F]{3,8}|(?<![0-9])[0-9]+(\.[0-9]+)?(px|\.dp)"
"$TARGET" --exclude-dir={tokens,theme,styles} || true)
if [ -n "$MATCHES" ]; then
echo "[FAIL] Hardcoded tokens detected:"
echo "$MATCHES"
exit 1
fi
echo "[PASS] Zero hardcoded values detected."

2. 3. Prompt: Pre-flight Audit & Diagnostic
Prompt yêu cầu Agent tự quét hệ thống và xuất bảng chẩn đoán:

None‎
Thực hiện PRE-FLIGHT CHECK toàn bộ môi trường trước khi khởi chạy Phiên 2:

## 1. KIỂM TRA INPUT ASSETS:
- Xác minh sự tồn tại của @DESIGN.md, @tokens/primitives.tokens.json,
@tokens/semantics.light.tokens.json, @tokens/semantics.dark.tokens.json,
@models/components.model.yaml, @docs/PRODUCT.md.
- Xác nhận DESIGN.md có YAML frontmatter và các file tokens.json tuân thủ
W3C DTCG ($value, $type).
- Kiểm tra xem models/components.model.yaml đã có đầy đủ block
platform_mapping (web, android) chưa.

## 2. KIỂM TRA AGENT SKILLS:
- Xác nhận khả năng nhận diện và thực thi các slash commands: /tdd,
/implement-spec, /impeccable-harden, /impeccable-polish, /impeccable-critique,
/code-review.

## 3. KIỂM TRA TOOLING & LIBS:
- Web: Kiểm tra trong package.json các packages @ladle/react (hoặc
Storybook) và @playwright/test.
- Android: Kiểm tra trong build.gradle.kts plugin Paparazzi
(app.cash.paparazzi), Showkase (airbnb/Showkase), và Android CLI kết nối adb.

## 4. KIỂM TRA HYGIENE & LINTER:
- Kiểm tra .gitignore đã chặn: .screenshots/, build/reports/paparazzi/,
app/build/reports/paparazzi/.
- Kiểm tra script scripts/lint-tokens.sh đã tồn tại và có quyền thực thi.

## ĐẦU RA:
In ra bảng chẩn đoán:
| Hạng mục | Trạng thái (PASS / FAIL / MISSING) | Chi tiết |
Nếu có mục FAIL/MISSING, dừng lại và yêu cầu bootstrap. Không tự ý sang Step 1.

2. 4. Prompt: Auto-Bootstrap & Remediation
Prompt yêu cầu Agent tự động khắc phục các mục bị thiếu:

None‎
Dựa trên bảng Pre-flight Check vừa thực hiện:

Hãy tự động thực hiện các hành động sau để đưa hệ thống về trạng thái PASS:
1. Thêm vào .gitignore:
.screenshots/
build/reports/paparazzi/
app/build/reports/paparazzi/
2. Tạo script scripts/lint-tokens.sh theo đúng mẫu tại Mục 2.2 của tài liệu này
(mô phỏng logic rule no-arbitrary-value từ repo GitHub
schoero/eslint-plugin-tailwindcss và slackhq/compose-lints). Cấp quyền chmod +x
scripts/lint-tokens.sh.
3. Nếu thiếu thư viện:
- Web: Tham khảo docs từ repo GitHub ladle-dev/ladle và microsoft/playwright
để chạy lệnh cài đặt package phù hợp (pnpm add -D @ladle/react
@playwright/test).
- Android: Tham khảo cấu hình mẫu từ repo GitHub cashapp/paparazzi và
airbnb/Showkase để thêm đúng block plugin/dependency vào build.gradle.kts và
libs.versions.toml.
4. Chạy lại kiểm tra và thông báo: [READY FOR STEP 1].

## 3. SEVEN-STEP EXECUTION PIPELINE & FULL PROMPTS

### Step 0: Session Setup Prompt
Khóa vai trò và nguyên tắc ngay đầu phiên:

None‎
Bạn đóng vai trò Lead Frontend / Android Engineer trong Phiên 2 (Production
Code & Visual Loop).
Nhiệm vụ: Hiện thực hóa component từ spec, viết test TDD và điều phối thẩm định
đối kháng qua 2 Sub-agent.

## RÀNG BUỘC CỐT LÕI:

#### 1. Đọc kỹ @DESIGN.md, @tokens/semantics.light.tokens.json,
@tokens/semantics.dark.tokens.json và @models/components.model.yaml làm kim chỉ
nam duy nhất.
2. ZERO HARDCODE: Cấm dùng mã Hex (#...), pixel hoặc dp tự do ngoài token.
3. Đúng phạm vi contract: Không tự ý thêm props hay variants ngoài spec. Bám
sát platform_mapping.
4. ONE-WAY FREEZE: Spec từ Phiên 1 là Read-Only. Cấm tự ý sửa DESIGN.md hay
model contract. Nếu thiếu spec, dừng lại báo lỗi "Spec Drift".
5. DUAL SUB-AGENT VETO GATE: Bắt buộc dispatch 2 Sub-agent (Vision Auditor qua
/impeccable-critique & Code Auditor qua /code-review) ở ngữ cảnh cô lập để
nghiệm thu. Cấm Agent chính tự kết luận PASS.
6. STRICT READ-ONLY AUDITOR: Sub-agent chỉ lập Deficiency Report và vote
PASS/REJECT, tuyệt đối không sửa code.
Xác nhận đã hiểu và sẵn sàng nhận lệnh Step 1.

### Step 1: Token Compilation
Biên dịch tokens sang hạ tầng code cho cả Light Mode và Dark Mode.

Prompt Web (Tailwind / CSS Variables):

None‎
Đọc @DESIGN.md, @tokens/semantics.light.tokens.json và
@tokens/semantics.dark.tokens.json (tham chiếu repo
schoero/eslint-plugin-tailwindcss):
Hãy biên dịch Design Tokens thành mã nguồn:
1. Tạo file `styles/tokens.css` chứa CSS Custom Properties:
- `:root`: ánh xạ toàn bộ biến từ `tokens/semantics.light.tokens.json`.
- `[data-theme='dark']`: ghi đè các biến tương ứng từ
`tokens/semantics.dark.tokens.json`.
2. Tạo file `tailwind.config.ts` ánh xạ 100% theme color, spacing scale (lưới
4px), radius và elevation từ `tokens.css`.
3. RÀNG BUỘC: Không tự ý sinh thêm token ngoài danh mục đã định nghĩa.

Prompt Android (Jetpack Compose Theme):

None‎
Đọc @DESIGN.md, @tokens/semantics.light.tokens.json và
@tokens/semantics.dark.tokens.json (tham chiếu repo slackhq/compose-lints):
Hãy sinh các file theme Jetpack Compose vào package `ui.theme`:
1. `Color.kt`: Khai báo 2 bảng màu riêng biệt `LightColorScheme` và
`DarkColorScheme` ánh xạ từ 2 file tokens tương ứng.
2. `Type.kt`: Cấu hình Typography theo Modular Scale trong spec.
3. `Theme.kt`: Cung cấp Composable `AppTheme` tự động chuyển đổi giữa
`LightColorScheme` và `DarkColorScheme` dựa trên `isSystemInDarkTheme()`.
4. RÀNG BUỘC: Cấm hardcode trực tiếp giá trị màu `Color(0x...)` ngoài file định
nghĩa theme.

### Step 2: Spec-to-Test (TDD Red Phase)
Viết test trước khi code component, bám sát platform_mapping.

Prompt chung:

None‎
/tdd
Đọc hợp đồng linh kiện của [Tên Component] trong @models/components.model.yaml:
Hãy viết test suite ([Component].test.tsx cho Web hoặc [Component]Test.kt cho
Android):
1. Render Tests: Kiểm tra đủ variants và sizes theo contract.
2. State Matrix Tests (Áp dụng đúng `platform_mapping` cho nền tảng hiện tại):
- Trạng thái `disabled`: kiểm tra cờ vô hiệu hóa (`disabled` trên Web,
`!enabled` trên Android), chặn click event.
- Trạng thái `loading`: kiểm tra cờ hiển thị spinner (`aria-busy` trên Web,
`isLoading` trên Android), ẩn/khóa label.
3. Constraint Tests: Assertion fail nếu vi phạm quy tắc UX (ví dụ duplicate
Primary Action trong cùng group).
RÀNG BUỘC: Toàn bộ test suite này phải ở trạng thái FAIL (Red phase). Chưa viết
code thực thi UI.

### Step 3: Component Implementation (Green Phase)
Viết mã nguồn linh kiện pass test.

Prompt chung:

None‎
/implement-spec
Hãy viết mã nguồn cho linh kiện [Tên Component] ([Component].tsx hoặc
[Component].kt):
### 1. Đáp ứng 100% test cases đã viết ở Step 2 để chuyển toàn bộ bài test sang
## PASS.
2. Hỗ trợ đầy đủ các slots: leading-icon, label, trailing-icon theo contract.
3. Sử dụng 100% biến/class đã sinh ở Step 1.
RÀNG BUỘC: Tuyệt đối không hardcode giá trị hex/px/dp. Chạy `bash
scripts/lint-tokens.sh` phải exit 0.

### Step 4: Preview Canvas Construction
Tạo canvas ma trận trạng thái trên 1 khung nhìn duy nhất.

Prompt Web (Ladle Preview Matrix):

None‎
Đọc @models/components.model.yaml và component [Tên Component] vừa viết ở Step
3:
Hãy tạo file preview ma trận trạng thái
`src/components/[Component].preview.tsx` (chuẩn tự động nhận diện của Ladle):
1. Bố trí một Grid Layout hiển thị đồng thời TẤT CẢ các trạng thái trên cùng 1
khung nhìn duy nhất:
- Cột: Default, Hover, Focus, Disabled, Loading, Error.
- Hàng: Từng variant x từng size theo contract.
2. Nền hiển thị sử dụng token `surface.canvas`. Bọc container hỗ trợ chuyển đổi
kiểm tra được cả Light Mode và Dark Mode.
3. RÀNG BUỘC: Không tự thêm logic thừa ngoài việc render ma trận component.

Prompt Android (Showkase / Paparazzi Preview Matrix):

None‎
Đọc @models/components.model.yaml và component [Tên Component] vừa viết ở Step
3:
Hãy tạo file preview ma trận trạng thái `ui/components/[Component]Preview.kt`
gắn annotation `@Preview`:

1. Bố trí một Composable Canvas dạng Column/Row hiển thị đầy đủ ma trận trạng
thái trên 1 màn hình:
- Variants x Sizes x States (Default, Disabled, Loading...).
- Đặt song song 2 container: Light Mode và Dark Mode (`AppTheme(darkTheme =
true/false)`).
### 2. Đảm bảo Composable này render độc lập, không phụ thuộc Context runtime để
Paparazzi chụp headless snapshot.

### Step 5: Headless Visual Capture
Chạy script headless tự động xuất snapshot và kiểm tra sự tồn tại của file ảnh.

Prompt Web (Playwright Headless Capture):

None‎
Khởi động preview server ngầm và chạy lệnh Playwright snapshot (tham chiếu repo
microsoft/playwright):
1. Chạy lệnh:
npx playwright test tests/visual.spec.ts --project=chromium
## 2. KIỂM TRA TỒN TẠI FILE ẢNH (ARTIFACT VERIFICATION):
- Kiểm tra xem file `.screenshots/web/[component]-matrix.png` đã được sinh
ra chưa.
- Nếu file không tồn tại hoặc kích thước 0 byte: Báo [FAIL: Snapshot
missing] và dừng lại khắc phục, KHÔNG ĐƯỢC CHUYỂN SANG STEP 6.
- Nếu file hợp lệ: Báo [PASS: Visual snapshot ready for Audit].

Prompt Android (Paparazzi Headless Capture):

None‎
Dùng Android CLI chạy lệnh terminal record snapshot Paparazzi (tham chiếu repo
cashapp/paparazzi):
1. Chạy lệnh:
./gradlew recordPaparazziDebug
## 2. KIỂM TRA TỒN TẠI FILE ẢNH (ARTIFACT VERIFICATION):
- Kiểm tra thư mục `app/build/reports/paparazzi/images/` xem các ảnh
`[Component]Preview_*.png` đã được sinh ra đầy đủ chưa.
- Nếu thư mục rỗng hoặc thiếu ảnh: Báo [FAIL: Paparazzi snapshot missing] và
dừng lại sửa lỗi build, KHÔNG ĐƯỢC CHUYỂN SANG STEP 6.

- Nếu file hợp lệ: Báo [PASS: Visual snapshot ready for Audit].

### Step 6: Autonomous Dual Sub-Agent Dispatch Protocol (Antagonistic Review
Gate)
Chỉ thị điều phối bắt buộc dành cho Agent chính sau khi hoàn thành Step 5:
Agent chính TUYỆT ĐỐI KHÔNG TỰ KẾT LUẬN PASS/REJECT và KHÔNG YÊU CẦU NGƯỜI
## DÙNG COPY-PASTE THỦ CÔNG.
Agent chính BẮT BUỘC tự động kích hoạt tool dispatch song song 2 Sub-agent độc lập với
Fresh Context (ngữ cảnh cô lập hoàn toàn, không truyền lịch sử trò chuyện):

1. Tự động Dispatch Sub-agent 1: Vision & UX Auditor
- Cơ chế khởi tạo: Agent chính gọi tool dispatch sub-agent với fresh context window.
- Payload đóng gói tự động:
  - rules: File @DESIGN.md (Hệ thống lưới 4px, thang màu, typography, WCAG).
  - artifact: File ảnh PNG snapshot tại
.screenshots/web/[component]-matrix.png (Web) hoặc
app/build/reports/paparazzi/images/[Component]Preview_*.png
(Android).
- Directives giao cho Sub-agent 1:
  - Kích hoạt skill /impeccable-critique.
  - Vai trò: Thẩm định viên thị giác đối kháng độc lập (Strict Read-Only Auditor).
## TUYỆT ĐỐI CẤM TỰ SỬA CODE.
  - Soi lỗi định lượng: Visual hierarchy, baseline căn gióng icon-text, khoảng cách
lưới 4px, độ tương phản WCAG 2.1 AA (cả light & dark theme), touch target >=
44x44px, clipping vỡ khung.
  - Đầu ra bắt buộc: Bảng Deficiency Report (Vị trí | Lỗi vi phạm định lượng | Spec
yêu cầu | Mức độ P0/P1/P2) và chốt đúng 1 từ: [PASS] hoặc [REJECT].

2. Tự động Dispatch Sub-agent 2: Spec & Code Auditor
- Cơ chế khởi tạo: Agent chính gọi tool dispatch sub-agent với fresh context window.
- Payload đóng gói tự động:
  - rules: File @models/components.model.yaml (Contract, Props, Variants, Slots,
Constraints, platform_mapping).
  - artifact: Mã nguồn [Component].tsx / [Component].kt và output lệnh git
diff.
- Directives giao cho Sub-agent 2:
  - Kích hoạt skill /code-review.

  - Vai trò: Kiểm toán viên mã nguồn đối kháng độc lập (Strict Read-Only Auditor).
## TUYỆT ĐỐI CẤM TỰ SỬA CODE.
  - Soi 2 trục: Trục 1 (Spec Match: đúng props/variants/slots theo contract, ánh xạ
đúng cờ platform_mapping của Web/Android), Trục 2 (Standards & Hygiene: 0
hardcode hex/px/dp, zero dead code, zero code smell).
  - Đầu ra bắt buộc: Bảng Deficiency Report (Dòng code/Thuộc tính | Lỗi vi phạm
contract | Spec yêu cầu | Mức độ P0/P1/P2) và chốt đúng 1 từ: [PASS] hoặc
## [REJECT].

### Step 7: Autonomous Self-Healing Remediation Loop & Circuit Breaker
Cơ chế tự sửa lỗi khép kín tự hành 100% của Agent chính (Zero Human-in-the-Loop):
7. Tiếp nhận kết quả & Luật phủ quyết (Veto Rule):
  - Nếu cả 2 Sub-agent cùng chốt [PASS]: Agent chính chạy bash
scripts/lint-tokens.sh lần cuối, tạo Git commit / Pull Request và thông báo
hoàn tất nhiệm vụ.
  - Nếu 1 trong 2 (hoặc cả 2) Sub-agent báo [REJECT]:
    - Agent chính tự động đọc danh sách lỗi trong bảng Deficiency Report.
    - Tự động kích hoạt skill /impeccable-harden hoặc
/impeccable-polish để sửa trực tiếp lỗi trong mã nguồn.
    - Tự động chạy lại Step 5 (chụp lại ảnh snapshot mới).
    - Tự động kích hoạt lại Step 6 (dispatch lại 2 Sub-agent mới với fresh
context để thẩm định lại).
8. Khóa ngân sách lặp & Cầu chì ngắt mạch (Circuit Breaker):
  - Ngân sách sửa lỗi tự động tối đa: 3 vòng lặp (Retry Budget <= 3).
  - Cầu chì ngắt mạch (Human Circuit Breaker): Chỉ khi sau 3 vòng lặp tự sửa mà 2
Sub-agent vẫn kiên quyết đóng dấu [REJECT], Agent chính mới ngắt mạch tự
động, dừng quy trình và xuất báo cáo đối soát 3 lần kèm hình ảnh/mã lỗi để xin
chỉ đạo từ người dùng. Không được dừng lại hỏi người dùng ở vòng 1 và 2.

## 4. BẢNG TIÊU CHÍ NGHIỆM THU (EXIT CRITERIA)
100% token được map từ @DESIGN.md, hỗ trợ cả Light & Dark mode (Pass script
scripts/lint-tokens.sh).
100% Unit test và Constraint test ở Step 2 đều PASS theo đúng platform_mapping.
File Preview Canvas thể hiện đầy đủ ma trận trạng thái trên 1 khung nhìn duy nhất.
Ảnh snapshot Playwright (Web) / Paparazzi (Android) khớp hoàn toàn với spec visual.
Dual Sub-Agent Consensus: Sub-agent 1 (Vision Auditor qua
/impeccable-critique) và Sub-agent 2 (Code Auditor qua /code-review) đều đóng
dấu [PASS].

Strict Read-Only Auditor: Không có tình trạng Sub-agent tự ý sửa mã nguồn.
Không có Spec Drift: Code bám sát 100% spec Phiên 1 mà không tự ý sửa file đặc tả.


## v3.0 ADDENDUM — SECURITY REVIEW GATE (MANDATORY)

After implementation and before the task can enter final arbitration, dispatch a
third independent Security Reviewer with fresh context. This reviewer is separate
from the Vision/UX and Spec/Code auditors. It receives the exact diff, base/head
SHAs, changed paths, relevant contracts, and SECURITY_REVIEW.md. It is read-only
and must not modify source, tests, configuration, snapshots, or baselines.

Required output:
- `.agy/security-review.json` with the schema and exact-head binding specified in
  SECURITY_REVIEW.md.
- A human-readable report at the path recorded in that JSON.
- Explicit results for secret scanning, dependency vulnerabilities, static/code
  security analysis, authorization/access-control tests where applicable, and
  network/mock-boundary verification where applicable.

No security dispatch or invalid/missing/stale evidence means BLOCKED. A failed check
or unresolved finding means FAIL. The Security Reviewer has an independent veto;
neither the primary agent nor the other auditors may override it. Security PASS is
required before commit/merge eligibility, PR-ready status, or final PASS.

Any code/configuration change during remediation invalidates all prior evidence.
Rerun the complete Phase 2 validation sequence (TDD/unit and state-matrix tests,
build/typecheck/lint, token constraints, fresh visual snapshots, both independent
auditors, and Security Reviewer) against the new head SHA. Do not reuse stale PASS
artifacts.

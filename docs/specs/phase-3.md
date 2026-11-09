# PHASE 3 — SCREEN ASSEMBLY, STATE WIRING & E2E VERIFICATION

> Converted from the supplied PDF. Source wording and sequence are retained; PDF page markers and extraction-only placeholders are omitted.

## PHASE 3 SPEC: SCREEN ASSEMBLY,
## STATE WIRING & E2E VERIFICATION
Agent Execution Specification & Full Copy-Paste Prompt Suite for Web & Android
Screen Assembly, State Management, Navigation, and End-to-End Testing.

## 1. INVARIANTS (HARD RULES)
1. 100% Component Reuse: Mọi màn hình bắt buộc lắp ghép từ các component
đã nghiệm thu ở Phiên 2 (Button, InputField, Card, Modal...). Nghiêm cấm tự tạo
lại thẻ button thô, input thô hoặc hardcode style CSS/Modifier tùy tiện bên
trong code màn hình.
2. Component Freeze Gate (Read-Only): Toàn bộ mã nguồn trong thư mục linh
kiện Phiên 2 (src/components/ hoặc ui/components/) là Read-Only đối với
Phiên 3. Cấm Agent tự ý sửa file component gốc. Nếu cần căn chỉnh padding,
margin hay responsive, chỉ được áp dụng ở cấp độ bố cục màn hình cha
(Screen container).
3. Screen Spec Source: Cấu trúc, danh sách linh kiện cần import và thứ tự hiển thị
của màn hình bắt buộc đọc từ mục Screen Hierarchy & Layouts trong
@docs/PRODUCT.md. Cấm Agent tự sáng tác thêm bớt section ngoài tài liệu này.
4. Four Mandatory Screen States: Mọi trang/màn hình bắt buộc xử lý trọn vẹn 4
trạng thái:
  - Loading: Hiển thị Skeleton hoặc Shimmer token-aligned.
  - Data (Success): Render dữ liệu chính xác theo layout responsive.
  - Empty: Hiển thị thông điệp và nút kêu gọi hành động (Call to Action) rõ
ràng.
  - Error: Hiển thị thông báo thân thiện kèm nút thử lại (Retry action).
5. Mock Fixtures Strategy: Bắt buộc thiết lập tầng dữ liệu giả lập cục bộ (JSON
Mock cho Web, Fake Repositories/In-memory DataSource cho Android) để
chạy màn hình và test luồng E2E độc lập 100%, không phụ thuộc vào kết nối
backend thật.
6. Canonical Icon Libraries:
  - Web: 100% icon lấy từ repo lucide-icons/lucide (lucide-react).
  - Android: 100% icon lấy từ thư viện
androidx.compose.material:material-icons-extended.

  - Cấm tự vẽ vector SVG tự do hoặc nhúng file icon ngoài spec.
7. End-to-End (E2E) Pass Gate: Màn hình chỉ được coi là hoàn tất khi vượt qua
toàn bộ kịch bản kiểm thử hành trình người dùng (User Journeys):
  - Web: Chạy microsoft/playwright E2E headless.
  - Android: Chạy mobile-dev-inc/maestro (Maestro CLI flows) trên thiết
bị/máy ảo thật.
8. Zero Design Drift: Toàn bộ màn hình lắp ráp không được vi phạm quy chuẩn
thiết kế. Chạy skill @egm-drift-report đối soát mã nguồn với DESIGN.md phải
đạt kết quả Zero Drift.

## 3. SIX-STEP EXECUTION PIPELINE & FULL PROMPTS

#### 2.0. Danh mục GitHub Repositories & Agent Skills tham chiếu
- Lắp ráp bố cục màn hình: Next.js App Router (Web) / Android Scaffold
(Compose). Kỹ năng: /implement-spec, /impeccable-adapt.
- Xử lý 4 States & Mock Data: pmndrs/zustand (Web) / Jetpack ViewModel
(Android). Kỹ năng: /impeccable-harden, /impeccable-onboard.
- Thư viện Icon chuẩn: lucide-icons/lucide (lucide-react cho Web) /
androidx.compose.material:material-icons-extended (Android).
- Điều hướng & Hiệu ứng chuyển cảnh: Motion tokens trong @DESIGN.md. Kỹ
năng: /impeccable-animate.
- Kiểm thử E2E người dùng: microsoft/playwright (Web) /
mobile-dev-inc/maestro (Maestro CLI cho Android).
- Tối ưu hiệu năng giao diện: Lighthouse / Compose Tracing. Kỹ năng:
/impeccable-optimize.
- Chống trôi lệch & Review kép: Kỹ năng: @egm-drift-report, /code-review.

#### 2.1. File & Directory Setup Checklist
Xác minh sự tồn tại của các tài sản đầu vào trước khi thực thi:
- @DESIGN.md (SSOT từ Phiên 1, Read-Only)
- @docs/PRODUCT.md (Chứa mục Screen Hierarchy & Layouts)
- @tokens/semantics.light.tokens.json &
@tokens/semantics.dark.tokens.json
- @models/components.model.yaml (Component contracts có
platform_mapping)

- Thư mục linh kiện đã nghiệm thu từ Phiên 2 (src/components/ cho Web hoặc
ui/components/ cho Android, Read-Only)
- Cấu trúc thư mục Phiên 3:
  - Web: src/screens/, src/mocks/, tests/e2e/
  - Android: ui/screens/, data/mocks/, ui/navigation/, .maestro/

#### 2.2. Automated Workspace Bootstrap Script
File script scripts/bootstrap-phase3.sh khởi tạo hạ tầng kiểm thử, thư mục mock
và cấu hình:

Shell‎
#!/usr/bin/env bash
set -euo pipefail

echo "=== Khởi tạo workspace Phiên 3 (Screen Assembly & E2E) ==="

# 1. Tạo thư mục màn hình, mock data và test luồng
mkdir -p tests/e2e .maestro src/mocks data/mocks scripts

# 2. Tạo template cấu hình Maestro cho Android (nếu chưa có)
if [ ! -f .maestro/app-flow.yaml ]; then
cat << 'EOF' > .maestro/app-flow.yaml
appId: com.example.app
---
- launchApp
- assertVisible: ".*"
## EOF
fi

# 3. Tạo template Playwright E2E cho Web (nếu chưa có)
if [ ! -f tests/e2e/journey.spec.ts ]; then
cat << 'EOF' > tests/e2e/journey.spec.ts
import { test, expect } from '@playwright/test';

test('Smoke test user journey with mock data', async ({ page }) => {
await page.goto('/');
await expect(page).toHaveTitle(/.+/);
});

## EOF
fi

echo "[PASS] Khởi tạo thư mục, mock data và template E2E thành công."

2. 3. Prompt: Pre-flight Audit & Diagnostic
Prompt yêu cầu Agent tự quét hệ thống và xuất bảng chẩn đoán:

None‎
Thực hiện PRE-FLIGHT CHECK toàn bộ môi trường trước khi khởi chạy Phiên 3:

## 1. KIỂM TRA INPUT ASSETS TỪ PHIÊN 1 & PHIÊN 2:
- Xác minh @docs/PRODUCT.md đã có mục "Screen Hierarchy & Layouts" mô tả chi
tiết các màn hình cần dựng.
- Xác nhận thư mục components từ Phiên 2 đã pass toàn bộ unit test và đang ở
trạng thái Read-Only.
- Xác nhận @DESIGN.md và 2 file tokens (@tokens/semantics.light.tokens.json,
@tokens/semantics.dark.tokens.json) là Read-Only.

## 2. KIỂM TRA THƯ VIỆN & CÔNG CỤ (LIBS & TOOLING):
- Icon: Kiểm tra package lucide-react (Web) hoặc dependency
material-icons-extended trong build.gradle.kts (Android).
- E2E Testing Web: Kiểm tra Playwright config đã sẵn sàng.
- E2E Testing Android (ADB Check): Chạy `adb devices`. Nếu không phát hiện
thiết bị hoặc máy ảo nào đang chạy, báo cáo MISSING kèm hướng dẫn: "Khởi động
Android Emulator hoặc cắm điện thoại bật USB Debugging trước khi chạy Maestro".

## 3. KIỂM TRA AGENT SKILLS:
- Xác nhận khả năng nhận diện và thực thi các slash commands/skills:
/implement-spec, /impeccable-adapt, /impeccable-harden, /impeccable-onboard,
/impeccable-animate, /impeccable-optimize, @egm-drift-report, /code-review.

## ĐẦU RA:
In ra bảng chẩn đoán:
| Hạng mục | Trạng thái (PASS / FAIL / MISSING) | Chi tiết |
Nếu có mục FAIL/MISSING, dừng lại và yêu cầu bootstrap. Không tự ý sang Step 1.

2. 4. Prompt: Auto-Bootstrap & Remediation
Prompt yêu cầu Agent tự động khắc phục các mục bị thiếu:

None‎
Dựa trên bảng Pre-flight Check vừa thực hiện:

Hãy tự động thực hiện các hành động sau để đưa hệ thống về trạng thái PASS:
1. Tạo thư mục cần thiết:
- Web: mkdir -p src/screens src/mocks tests/e2e
- Android: mkdir -p app/src/main/java/.../ui/screens data/mocks .maestro
2. Bổ sung thư viện thiếu (nếu chưa có):
- Web: `pnpm add lucide-react && pnpm add -D @playwright/test`
- Android: Thêm block dependency
`androidx.compose.material:material-icons-extended` và
`androidx.navigation:navigation-compose` vào build.gradle.kts.
3. Nếu thiếu ADB Device (Android): Hiển thị thông báo nhắc người dùng bật máy
ảo Android Emulator.
4. Chạy lại kiểm tra và thông báo: [READY FOR STEP 1].

## 3. FIVE-STEP EXECUTION PIPELINE & FULL PROMPTS

### Step 0: Session Setup Prompt
Khóa vai trò và nguyên tắc ngay đầu phiên:

None‎

## RÀNG BUỘC CỐT LÕI:
1. 100% COMPONENT REUSE: Tái sử dụng linh kiện từ Phiên 2. CẤM SỬA FILE GỐC
TRONG THƯ MỤC COMPONENTS/ (Component Freeze Gate).
2. SCREEN SPEC CHUẨN: Đọc cấu trúc bố cục bắt buộc từ mục "Screen Hierarchy &
Layouts" trong @docs/PRODUCT.md.
3. BẮT BUỘC ĐỦ 4 STATES: Mọi màn hình phải xử lý trọn vẹn Loading, Data, Empty,
Error (kèm nút Retry).
4. MOCK DATA ĐẦU ĐỦ: Tạo mock fixtures để chạy độc lập không cần backend thật.
5. ICON CHUẨN: Dùng đúng Lucide (Web) hoặc Material Icons (Android).

6. PASS E2E TEST: Màn hình phải pass kịch bản Playwright (Web) hoặc Maestro CLI
(Android).
Xác nhận đã hiểu và sẵn sàng nhận lệnh Step 1.

### Step 1: Screen Layout Assembly
Lắp ghép bố cục màn hình từ thư viện linh kiện Phiên 2 theo đặc tả từ PRODUCT.md.

Prompt Web (Next.js / Responsive Layout):

None‎
/implement-spec
/impeccable-adapt
Đọc mục "Screen Hierarchy & Layouts" trong @docs/PRODUCT.md, @DESIGN.md, và các
component trong thư mục components/:
Hãy lắp ghép bố cục cho màn hình [Tên Màn Hình - ví dụ DashboardScreen]:
1. Sử dụng 100% components từ Phiên 2 (Button, Card, InputField, Modal...). Cấm
sửa code bên trong thư mục components/.
### 2. Áp dụng quy chuẩn fluid layout và responsive breakpoints (Mobile 375px,
Tablet 768px, Desktop 1440px):
- Header bar, Navigation Drawer/Sidebar, Content Grid theo đúng thứ tự trong
PRODUCT.md.
3. Sử dụng icon từ repo lucide-icons/lucide (lucide-react).
#### 4. Đảm bảo touch targets tối thiểu 44x44px cho tất cả các điểm tương tác chạm.
5. RÀNG BUỘC: Tuyệt đối không hardcode giá trị hex/px tự do. 100% khoảng cách
padding/gap bám sát lưới 4px.

Prompt Android (Scaffold & Adaptive Layout):

None‎
/implement-spec
/impeccable-adapt
Đọc mục "Screen Hierarchy & Layouts" trong @docs/PRODUCT.md, @DESIGN.md, và các
component trong package ui.components:
Hãy xây dựng Composable cho màn hình [Tên Màn Hình - ví dụ DashboardScreen]:

1. Sử dụng Scaffold cung cấp topBar, bottomBar, và floatingActionButton bằng
components Phiên 2. Cấm sửa code trong ui/components/.
2. Bố trí Column / LazyColumn với spacing tuân thủ token theo cấu trúc trong
PRODUCT.md.
3. Tích hợp icon từ androidx.compose.material:material-icons-extended.
4. Hỗ trợ Adaptive Window Size Classes (Compact cho điện thoại, Expanded cho
tablet/foldable).
5. RÀNG BUỘC: Cấm hardcode màu sắc Color(...) hoặc dp tự do ngoài theme.

### Step 2: State Management, Mock Fixtures & 4-State Wiring
Tạo dữ liệu giả lập và nối trạng thái giao diện an toàn.

Prompt Web (Zustand / React Hooks + JSON Mocks):

None‎
/impeccable-harden
/impeccable-onboard
1. TẠO MOCK FIXTURES (`src/mocks/[screen].mock.ts`):
- Xuất dữ liệu giả lập cho 2 kịch bản: `mockSuccessData` (danh sách đầy đủ)
và `mockEmptyData` (mảng rỗng []).
- Hàm giả lập API có cờ toggle giả lập lỗi mạng (Error 500).

## 2. XÂY DỰNG TẦNG STATE MANAGEMENT:
- Khởi tạo store quản lý trạng thái màn hình với đầy đủ 4 trạng thái:
+ `isLoading`: Render Skeleton/Shimmer matching layout.
+ `data`: Render danh sách dữ liệu từ mock.
+ `isEmpty`: Dựng Empty State chuẩn UX (minh họa, tiêu đề, mô tả và CTA
tạo mới).
+ `error`: Render Error Banner/Modal kèm nút Retry gọi lại hàm fetch dữ
liệu.
- Gia cố biên: Xử lý an toàn trường hợp dữ liệu null, mảng rỗng, hoặc chuỗi
text quá dài.
- Nối action tương tác (click, submit, delete) vào các callback handler của
component.

Prompt Android (ViewModel, StateFlow & Fake Repository):

None‎
/impeccable-harden
/impeccable-onboard
1. TẠO FAKE REPOSITORY (`data/mocks/Fake[Screen]Repository.kt`):
- Cung cấp dữ liệu mẫu cho trạng thái Success và Empty.
- Thêm cờ `shouldReturnError = true` để giả lập ném Exception.

## 2. XÂY DỰNG VIEWMODEL:
- Khởi tạo `[Tên]UiState` dạng sealed interface:
+ `Loading`: Hiển thị Shimmer loading.
+ `Success(val data: List<...>)`: Hiển thị danh sách dữ liệu.
+ `Empty(val title: String, val message: String)`: Dựng Empty State với
CTA kích hoạt.
+ `Error(val message: String)`: Hiển thị giao diện báo lỗi kèm nút Thử
lại.
- Expose `StateFlow<[Tên]UiState>` từ `[Tên]ViewModel`.
- Trong Composable màn hình: Dùng `collectAsStateWithLifecycle()` và
switch-case render chính xác 4 trạng thái tương ứng.

### Step 3: Navigation & Route Flow
Cấu hình định tuyến và gán hiệu ứng chuyển cảnh mượt mà.

Prompt Web (App Router / Navigation Flow):

None‎
/impeccable-animate
Cấu hình Route và Navigation cho màn hình [Tên Màn Hình]:
1. Khai báo route trong Next.js App Router kèm validation params (ID, slug,
query).
2. Thiết lập luồng chuyển trang (Page transitions) với thời gian transition và
easing curve lấy từ token motion trong @DESIGN.md.
3. Thêm micro-interactions cho các hiệu ứng xuất hiện danh sách (staggered list
animation).
4. Xử lý bảo vệ route (Protected routes, Redirect về Login nếu chưa xác thực).

Prompt Android (Navigation Compose):

None‎
/impeccable-animate
Cấu hình Navigation Compose cho màn hình [Tên Màn Hình]:
1. Khai báo NavGraph destination với type-safe route và arguments.
2. Xử lý sự kiện điều hướng (navigateToDetail, navigateBack).
3. Cấu hình hiệu ứng chuyển cảnh enterTransition và exitTransition
(slideIntoContainer, fade) theo đúng motion specs trong @DESIGN.md.

### Step 4: End-to-End (E2E) Journey Testing
Kiểm thử hành trình người dùng thực tế từ đầu đến cuối trên tầng Mock Fixtures.

Prompt Web (Playwright E2E):

None‎
Viết và thực thi kịch bản Playwright E2E cho [Tên Màn Hình] trong
tests/e2e/[screen].spec.ts (tham chiếu repo microsoft/playwright):
1. Kịch bản 1: Mở màn hình với mock success -> Kiểm tra hiển thị trạng thái
Loading -> Dữ liệu tải thành công.
2. Kịch bản 2: Mở màn hình với mock empty -> Kiểm tra hiển thị Empty State và
bấm nút CTA tạo mới.
3. Kịch bản 3: Tương tác người dùng (điền form, click submit, mở modal) -> Kiểm
tra kết quả hiển thị.
4. Kịch bản 4: Kích hoạt mock error -> Kiểm tra hiển thị Error screen và click
nút Retry.
5. Chạy lệnh: npx playwright test tests/e2e/[screen].spec.ts --project=chromium
YÊU CẦU: 100% assertions phải PASS.

Prompt Android (Maestro CLI Flow):

None‎
Viết và thực thi kịch bản Maestro Flow cho [Tên Màn Hình] trong
`.maestro/[screen]-flow.yaml` (tham chiếu repo `mobile-dev-inc/maestro`):
1. Khởi động app: `launchApp`
2. Chờ màn hình tải xong: `assertVisible: "[Tên phần tử đặc trưng]"`
3. Chạm vào component tương tác: `tapOn: "[Tên nút/Action]"`
4. Kiểm tra điều hướng chuyển màn hình thành công.
5. Chạy lệnh qua Android CLI: `maestro test .maestro/[screen]-flow.yaml`

YÊU CẦU: Luồng kiểm thử tự động đạt kết quả PASS hoàn toàn trên thiết bị/máy
ảo.

### Step 5: Optimization & Autonomous Dual Sub-Agent Dispatch Protocol
Agent chính TUYỆT ĐỐI KHÔNG TỰ KẾT LUẬN PASS/REJECT và KHÔNG YÊU CẦU
## NGƯỜI DÙNG COPY-PASTE THỦ CÔNG.
Sau khi hoàn thành Step 4 (E2E Test) và chạy tối ưu hiệu năng, Agent chính BẮT BUỘC
tự động kích hoạt tool dispatch song song 2 Sub-agent độc lập với Fresh Context (ngữ
cảnh cô lập hoàn toàn, không kèm lịch sử chat):

1. Tối ưu hóa hiệu năng giao diện (Agent chính tự chạy)
Agent chính kích hoạt:

None‎
/impeccable-optimize
- Web: Rà soát layout shift (CLS), khử re-render thừa, đảm bảo Lighthouse
Performance & A11y >= 90.
- Android: Soát re-composition thừa trong LazyColumn, đảm bảo tốc độ cuộn ổn
định 60/120fps.

2. Tự động Dispatch Sub-agent 1: Screen UX & Drift Auditor
- Cơ chế khởi tạo: Agent chính gọi tool dispatch sub-agent với fresh context
window.
- Payload đóng gói tự động:
  - rules: File @DESIGN.md (Hệ thống lưới, thang màu, font chữ) và mục
Screen Hierarchy & Layouts trong @docs/PRODUCT.md.
  - artifact: Ảnh chụp màn hình thực tế (Mobile & Desktop).
- Directives giao cho Sub-agent 1:
  - Kích hoạt skills: /impeccable-critique và @egm-drift-report.
  - Vai trò: Kiểm toán viên Trải nghiệm & Độ lệch Thiết kế Độc lập (Strict
Read-Only Auditor). TUYỆT ĐỐI CẤM TỰ SỬA CODE.
  - Soi lỗi định lượng:
    - Structural Drift: So khớp cây bố cục thực tế với mục Screen
Hierarchy & Layouts trong PRODUCT.md. Bắt lỗi tự ý thêm/bớt
section.

    - Mandatory 4-States: Kiểm tra đầy đủ hiển thị an toàn của 4 trạng
thái (Loading, Data, Empty, Error).
    - Responsive & Touch Bounds: Bắt lỗi tràn khung, đè nút, touch
target < 44x44px trên mobile.
  - Đầu ra bắt buộc: Bảng Deficiency Report (Vị trí/State | Lỗi vi phạm định
lượng | Spec yêu cầu | Mức độ P0/P1/P2) và chốt đúng 1 từ: [PASS] hoặc
## [REJECT].

3. Tự động Dispatch Sub-agent 2: Architecture & Component Freeze Auditor
- Cơ chế khởi tạo: Agent chính gọi tool dispatch sub-agent với fresh context
window.
- Payload đóng gói tự động:
  - rules: File @models/components.model.yaml.
  - artifact: Mã nguồn màn hình vừa ghép và output lệnh git diff.
- Directives giao cho Sub-agent 2:
  - Kích hoạt skill /code-review.
  - Vai trò: Kiểm toán viên Kiến trúc & Mã nguồn Độc lập (Strict Read-Only
Auditor). TUYỆT ĐỐI CẤM TỰ SỬA CODE.
  - Soi lỗi kiến trúc 2 trục:
    - Trục 1 (Spec Match & Component Freeze): BẮT BUỘC ZERO
MUTATION - Cấm sửa bất kỳ file nào trong thư mục components/
Phiên 2; cấm tự chế thẻ button/input thô; kiểm tra đủ 4 states và
mock fixtures.
    - Trục 2 (Standards & Hygiene): Quét rò rỉ mã hex (#...), pixel/dp
tùy tiện, exception handling an toàn, không rò rỉ bộ nhớ.
  - Đầu ra bắt buộc: Bảng Deficiency Report (Dòng code/File | Lỗi vi phạm
kiến trúc | Spec yêu cầu | Mức độ P0/P1/P2) và chốt đúng 1 từ: [PASS]
hoặc [REJECT].

### Step 6: Autonomous Self-Healing Remediation Loop & Circuit Breaker
Cơ chế tự sửa lỗi khép kín tự hành 100% của Agent chính (Zero Human-in-the-Loop):
#### 9. 1. Tiếp nhận kết quả & Luật phủ quyết (Veto Rule):
  - Nếu cả 2 Sub-agent cùng chốt [PASS]: Agent chính chạy
@egm-drift-report xác nhận Zero Drift lần cuối, tạo Git commit / Pull
Request và thông báo hoàn tất nhiệm vụ.
  - Nếu 1 trong 2 (hoặc cả 2) Sub-agent báo [REJECT]:
  - Agent chính tự động đọc danh sách lỗi trong bảng Deficiency Report.

    - Tự động kích hoạt skill /impeccable-harden hoặc
/impeccable-adapt để sửa trực tiếp code màn hình (TUYỆT ĐỐI
## KHÔNG SỬA VÀO THƯ MỤC COMPONENTS/).
    - Tự động chạy lại Step 4 (chạy lại test E2E).
    - Tự động kích hoạt lại Step 5 (dispatch lại 2 Sub-agent mới với
fresh context để thẩm định lại).
#### 10.2. Khóa ngân sách lặp & Cầu chì ngắt mạch (Circuit Breaker):
  - Ngân sách sửa lỗi tự động tối đa: 3 vòng lặp (Retry Budget <= 3).
  - Cầu chì ngắt mạch (Human Circuit Breaker): Chỉ khi sau 3 vòng lặp tự
sửa mà 2 Sub-agent vẫn kiên quyết đóng dấu [REJECT], Agent chính
mới ngắt mạch tự động, dừng quy trình và xuất báo cáo đối soát 3 lần
kèm hình ảnh/mã lỗi để xin chỉ đạo từ người dùng. Không được dừng lại
hỏi người dùng ở vòng 1 và 2.

## 4. BẢNG TIÊU CHÍ NGHIỆM THU (EXIT CRITERIA)
100% components trên màn hình được tái sử dụng từ Phiên 2 (Pass
/implement-spec).
Zero Component Mutation: Không có bất kỳ dòng code nào trong thư mục linh
kiện Phiên 2 (components/) bị thay đổi.
Cấu trúc màn hình bám sát 100% mục Screen Hierarchy & Layouts trong
@docs/PRODUCT.md.
Bố cục giao diện đáp ứng đa kích thước màn hình và touch target >= 44x44px
(Pass /impeccable-adapt).
Màn hình xử lý trọn vẹn 4 trạng thái: Loading, Data, Empty, Error kèm action
Retry qua Mock Fixtures (Pass /impeccable-harden &
/impeccable-onboard).
Hiệu ứng chuyển cảnh và tương tác tuân thủ motion tokens trong @DESIGN.md
(Pass /impeccable-animate).
100% icons được import từ repo chính thức: lucide-react (Web) hoặc
material-icons-extended (Android).
Toàn bộ kịch bản E2E User Journey (Playwright cho Web / Maestro CLI cho
Android) đều PASS độc lập trên tầng Mock.
Hiệu năng giao diện mượt mà, không giật cục (Pass /impeccable-optimize).

Dual Sub-Agent Consensus: Sub-agent 1 (Screen UX Auditor qua
/impeccable-critique & @egm-drift-report) và Sub-agent 2 (Architecture
Auditor qua /code-review) đều đóng dấu [PASS].
Strict Read-Only Auditor: Không có tình trạng Sub-agent tự ý sửa mã nguồn.
Báo cáo @egm-drift-report xác nhận Zero Drift so với @DESIGN.md.
  -


## v3.0 ADDENDUM — FULL REGRESSION AFTER EVERY REMEDIATION

The Step 6 remediation loop MUST NOT rerun only E2E and reviewers. Every source,
test, configuration, mock, navigation, or token-related change invalidates the
previous validation evidence. Before any reviewer is dispatched and before
ARBITRATION or PASS, execute the complete regression matrix for every affected
platform:

1. Clean dependency/configuration validation and production build.
2. Typecheck (Web) / Kotlin compilation and relevant static checks (Android).
3. Lint and formatting checks, including token/style constraints.
4. Unit tests for affected modules.
5. Full four-state/state-matrix tests: Loading, Data/Success, Empty, Error, and
   Retry behavior, including boundary/null/long-content cases where applicable.
6. Web Playwright E2E and/or Android Maestro E2E for all affected user journeys.
7. Fresh visual snapshot capture and baseline comparison (Playwright/Web and
   Paparazzi/Android); stale snapshots are invalid.
8. Component immutability check: prove Phase 2 component paths have zero diff.
9. Responsive/window-size, overflow, and touch-target checks on supported
   breakpoints/device classes.
10. Independent UX/Drift and Architecture/Code reviewers rerun with fresh context.
11. Independent Security Reviewer rerun with fresh context and exact head SHA.
12. Verify all reports are complete, current, and bound to the tested head SHA.

Each check must produce a durable evidence artifact with command, exit code,
timestamp, platform, commit SHA, and report path. A required check that is unsupported,
not configured, skipped, timed out, or missing its artifact is BLOCKED—not PASS.
A failed check is FAIL. A flaky check remains FLAKY and blocks release.

Only after the full matrix and all three independent reviews are PASS may the task
enter ARBITRATION. ARBITRATION is a pending decision, never a PASS state. Merge or
release remains blocked until the applicable human risk approval is recorded.

If remediation changes code after any regression step, restart the entire matrix
from step 1 against the new head SHA. Do not dispatch reviewers while mandatory
regression is incomplete. The retry budget remains at most three remediation rounds;
on exhaustion, stop and preserve artifacts for human intervention.

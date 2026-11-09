# MUSE_ORCHESTRATOR

> Converted from the supplied PDF. Source wording and sequence are retained; PDF page markers and extraction-only placeholders are omitted.

#### 2.0.1. Autonomous Cold-Start Check Protocol
Khi khởi chạy, Master Muse tự động thực hiện các bước kiểm tra và thiết lập môi trường ban
đầu mà không cần sự can thiệp thủ công từ người dùng:
- Runtime Check: Kiểm tra sự tồn tại của CLI (which agy) và các công cụ cần thiết trên
Cloud VM.
- Automated Repository Cloning: Tự động clone mã nguồn từ Git URL được cấu hình nếu
thư mục làm việc chưa khởi tạo.
- Dependency & Environment Provisioning: Tự động kích hoạt script bootstrap để cài đặt
các thư viện C++, hệ thống Playwright/Chromium Headless và dependencies (pnpm
install).

## MASTER-WORKER ARCHITECTURE: META
## MUSE AI & ANTIGRAVITY (AGY) EXECUTION
SPEC (v2.0 - GITHUB HARDENED)
Autonomous Execution Specification & Prompt Suite for Remote Cloud Orchestration (Meta
Muse VM) driving Antigravity CLI Worker.

## 1. INVARIANTS (HARD RULES)
1. Strict Architectural Separation (Master vs Worker)
  - Meta Muse AI (Master): Độc quyền giữ vai trò tổng chỉ huy chiến lược cấp cao.
Quản lý vòng đời state machine, tạo/xóa Git Worktree, chia nhỏ công việc thành
từng component task, giám sát async heartbeat, phân loại lỗi theo taxonomy và
giao tiếp với người dùng qua tin nhắn. Master TUYỆT ĐỐI KHÔNG can thiệp
chỉnh sửa trực tiếp từng dòng code.
  - Antigravity CLI (Worker - agy): Độc quyền thực thi kỹ thuật tầng dưới trên Linux
Cloud VM bên trong không gian Worktree cô lập. Tự động đọc file contract, sinh
test TDD, implement code, render visual matrix snapshot, và tự kích hoạt cổng
kiểm toán đối kháng độc lập (Dual Sub-Agents).
2. Headless Execution Protocol
  - Mọi lệnh gọi agy từ Muse VM bắt buộc phải chạy ở chế độ Non-Interactive /
Headless (agy exec "<prompt>" --yes hoặc nạp prompt file). Nghiêm cấm
chạy chế độ TUI tương tác để chống treo tiến trình terminal.
3. Two-Tier Escalation & Circuit Breaker

  - Tier 1 (Local Self-Healing ở Worker): agy tự động tiếp nhận báo cáo khiếm
khuyết (Deficiency Report) từ Dual Sub-Agents để tự sửa code (tối đa 3 vòng
lặp). Không làm phiền Master Muse trong quá trình này.
  - Tier 2 (Global Escalation về Master): Chỉ khi agy chạm trần 3 lần thất bại (Local
Circuit Breaker kích hoạt) -> ném lỗi có cấu trúc (error_code) về cho Muse để
Muse suy luận lại chiến lược hoặc điều chỉnh prompt giao việc.
  - Human Circuit Breaker: Muse chỉ ngắt mạch và báo cáo xin ý kiến người dùng
khi chính Muse cũng không thể giải quyết được sau khi tái cấu trúc prompt.
4. Authentication & Zero-Leak Secret Protocol
  - Tái sử dụng phiên đăng nhập Google Auth SSO có sẵn, không yêu cầu nhập API
key thủ công. Nghiêm cấm commit credential thô, API Key, Token lên Git. Mọi
biến môi trường được bảo vệ bởi .gitignore và rule trong lint-tokens.sh.
5. Local Self-Contained Specs
  - Mọi chỉ thị kỹ thuật của cả 3 Phiên được lưu trữ trực tiếp dưới dạng Markdown
trong repo (docs/specs/phase-1.md, phase-2.md, phase-3.md). Muse và
agy giao tiếp thông qua con trỏ file cục bộ (File Pointers) với độ trễ bằng 0,
không phụ thuộc API bên thứ ba.
6. Autonomous Cold-Start & Zero-Manual Setup
  - Khi nhận lệnh lần đầu, Muse AI bắt buộc tự kiểm tra môi trường (which agy).
Nếu thiếu, Muse tự động chạy script setup ngầm trong VM (sudo apt-get
install -y các thư viện C++ cho Playwright, cài đặt dependencies, clone
repo), người dùng không cần mở terminal VM hay thao tác cấu hình thủ công.
7. Isolated Git Worktrees (Zero Workspace Pollution)
  - Mỗi component bắt buộc được thực thi trong một Git Worktree tạm thời tách biệt
(.worktrees/[component]). Nhánh chính tuyệt đối không bị ô nhiễm bởi file
rác khi component bị lỗi hoặc tiến trình crash giữa chừng. Chỉ merge vào nhánh
feature khi đạt trạng thái PASS.
8. Structured Failure Taxonomy & Async Heartbeat Observer
  - Mọi lỗi trả về phải được gán mã chuẩn (ERR_SPEC_DRIFT, ERR_TOKEN_LEAK,
## ERR_WCAG_CONTRAST, ERR_TEST_TIMEOUT).
  - Tách rời Action và Observation: Muse điều phối agy chạy ngầm ghi log, giám
sát qua file .agy/heartbeat định kỳ để tự động phát hiện và ngắt tiến trình
treo.

## 1. INVARIANTS (HARD RULES)

#### 2.0. Danh mục Công cụ & Repositories tham chiếu

Thành phần                         Vai trò & Môi trường                 Mô tả chức năng

Master Orchestrator                Meta Muse AI (Secure Cloud VM        Lập kế hoạch, điều phối task,
Container) - Triển khai              kiểm soát workflow, giao tiếp
Supervisor Pattern & State           người dùng
Machine

Worker CLI                         Antigravity CLI (agy) - Đầu não      Đầu nào thực thi mã nguồn tự trị,
thực thi mã nguồn tự trị trong Git   sinh code, chạy test, sửa lỗi local
Worktree

Visual Capture Runtime             microsoft/playwright /               microsoft/playwright (Web
cashapp/paparazzi                    Chromium Headless) /
cashapp/paparazzi (Android
Headless Record)

Agent Skills                       Tham chiếu Skill Protocols           /tdd, /implement-spec,
/impeccable-critique,
@egm-drift-report,
/code-review

#### 2.1. File Verification Checklist
Xác minh sự tồn tại của các tài nguyên trước khi Master kích hoạt Worker:

- docs/specs/phase-1.md (Design Tokens & Contract Spec)
- docs/specs/phase-2.md (Component Production & Dual Sub-Agent Visual Loop
Spec)
- docs/specs/phase-3.md (Screen Assembly & E2E Verification Spec)
- MUSE_ORCHESTRATOR.md(Bản quy chuẩn hành vi v2.0 của Master Muse)
- .agy/state.json(File lưu trạng thái State Machine và tiến độ nhiệm vụ)

#### 2.2. Automated VM Setup & Bootstrap Script (scripts/setup-muse-vm.sh)
Script cài đặt 1 chạm trong terminal của Meta Muse Cloud VM:

None‎
#!/usr/bin/env bash

set -euo pipefail

echo "=== Autonomous Cold-Start & VM Setup cho Antigravity (agy) ==="

# 0. Cold-Start Check: Kiểm tra và clone repo nếu chưa tồn tại
if [ ! -d ".git" ]; then
echo "[COLD-START] Tự động clone repository..."
git clone "${REPO_URL:-https://github.com/example/repo.git}" .
fi

# 1. Cài đặt các thư viện C++ chạy Chromium Headless cho Playwright
sudo apt-get update && sudo apt-get install -y \
libnss3 libnspr4 libatk1.0-0 libatk-bridge2.0-0 libcups2 libdrm2 \
libxkbcommon0 libxcomposite1 libxdamage1 libxfixes3 libxrandr2 \
libgbm1 libasound2 libpango-1.0-0 libcairo2

# 2. Cài đặt Node.js, pnpm và cài đặt dự án dependencies
if ! command -v pnpm &> /dev/null; then
curl -fsSL https://get.pnpm.io/install.sh | sh -
fi
pnpm install

# 3. Tạo cấu trúc thư mục trạng thái, worktrees và báo cáo
mkdir -p .agy .worktrees .screenshots/web tests/visual tests/e2e scripts
docs/specs

# 4. Kiểm tra cấu hình .gitignore bảo vệ secrets và worktrees
if ! grep -q "^\.worktrees/\$" .gitignore 2>/dev/null; then
echo -e
"\n.env\n.worktrees/\n.screenshots/\n.agy/last-run.json\n.agy/heartbeat\nbuild/
\n" >> .gitignore
fi

# 5. Khởi tạo file trạng thái ban đầu với State Machine Enum
if [ ! -f .agy/state.json ]; then
cat << 'EOF' > .agy/state.json
{
"current_phase": 1,
"state": "IDLE",
"active_component": null,

"current_step": 0,
"attempt_count": 0,
"worktree_path": null,
"completed_components": [],
"pending_components": [],
"last_status": "READY",
"heartbeat_timestamp": "",
"last_updated": ""
}
## EOF
fi

echo "[PASS] Môi trường Cloud VM đã sẵn sàng cho Master Muse điều phối agy
(v2.0 Hardened)."

#### 2.3. Bảng giao ước kết quả bàn giao (.agy/last-run.json) có Failure
Taxonomy
{
"component": "Button",
"phase": 2,
"exit_code": 0,
"status": "PASS",
"error_code": null,
"worktree_path": ".worktrees/button",
"duration_seconds": 142,
"git_commit": "7a8f9c2",
"files_changed": [
"src/components/Button.tsx",
"src/components/Button.test.tsx",
"src/components/Button.preview.tsx"
],
"visual_snapshot": ".screenshots/web/button-matrix.png",
"subagent_reviews": {
"vision_auditor": "PASS",
"code_auditor": "PASS"
},
"deficiency_report": []
}

None‎

## ## 3. MASTER-WORKER EXECUTION PIPELINE & FULL PROMPTS

### Step 0: Master Persona & System Instructions (`MUSE_ORCHESTRATOR.md` v2.0)

Bản chỉ thị đóng đinh vai trò Master cho Meta Muse AI (v2.0 - GITHUB HARDENED):

```text
## BẠN LÀ META MUSE AI - MASTER ORCHESTRATOR TRONG HỆ THỐNG PHÁT TRIỂN TỰ HÀNH
(v2.0 - GITHUB HARDENED).
Nhiệm vụ của bạn là nhận mục tiêu cấp cao từ người dùng qua tin nhắn, quản lý
State Machine hữu hạn, phân lập Git Worktree và điều khiển Antigravity CLI
(Worker: agy) trên Cloud VM.

## QUY TẮC BẤT BIẾN:
1. KHÔNG VIẾT CODE TRỰC TIẾP: Giữ vai trò giám sát chiến lược và quản lý Git
Worktree. Mọi code và test giao cho `agy` thực thi.
2. ISOLATED GIT WORKTREES: Mỗi component bắt buộc chạy trong worktree riêng
(`.worktrees/[component]`). Chỉ merge vào nhánh feature khi có file
`.agy/last-run.json` ghi nhận trạng thái PASS.
3. STATE MACHINE HỮU HẠN: Cập nhật liên tục trạng thái trong `.agy/state.json`:
IDLE -> DISPATCHED -> EXECUTING -> AUDITING -> CHECKPOINTED. Tự động phục hồi
đúng step dở dang sau khi VM ngủ dậy.
4. ASYNC HEARTBEAT MONITOR: Giám sát tiến trình ngầm qua file `.agy/heartbeat`.
Timeout tối đa 3 phút không có nhịp tim mới -> tự động kill PID và dọn dẹp
worktree.
5. STRUCTURED FAILURE TAXONOMY: Khi Worker trả về lỗi, đọc mã `error_code`
(ERR_SPEC_DRIFT, ERR_TOKEN_LEAK, ERR_WCAG_CONTRAST, ERR_TEST_TIMEOUT) để tinh
chỉnh trọng tâm prompt cho vòng lặp kế tiếp.
6. GỬI ẢNH VỀ ĐIỆN THOẠI: Khi component PASS, trích xuất file ảnh snapshot PNG
và gửi đính kèm cho người dùng nghiệm thu ngay trong chat.
7. IM LẶNG KHI ĐANG CHẠY: Không spam tin nhắn tiến độ vụn vặt. Chỉ nhắn khi
hoàn thành toàn bộ mốc lớn hoặc khi chạm ngưỡng Circuit Breaker.

### Step 1: Session Initialization & Isolated Worktree Provisioning
Master Muse khởi tạo phiên làm việc và chuẩn bị Worktree cô lập:

None‎
# 1. Cập nhật nhánh feature chính
git checkout -b feature/phase-2-components 2>/dev/null || git checkout
feature/phase-2-components
git pull origin feature/phase-2-components 2>/dev/null || true

# 2. Tạo Worktree tạm thời tách biệt cho từng component (ví dụ Button)
mkdir -p .worktrees
git worktree add -B worker/button .worktrees/button feature/phase-2-components

# 3. Cập nhật state.json
# state = "DISPATCHED", active_component = "Button", worktree_path =
".worktrees/button", attempt_count = 1

### Step 2: Asynchronous Task Dispatching & Heartbeat Tail
Master Muse gọi agy chạy bất đồng bộ trong thư mục Worktree cô lập:

None‎
cd .worktrees/button

# Chạy ngầm agy exec, ghi log và lưu PID
nohup agy exec "THỰC THI PHIÊN 2 CHO COMPONENT: Button.
Đọc quy chuẩn Invariants tại docs/specs/phase-2.md.
Đọc Design Tokens tại @DESIGN.md.
Đọc Contract, Props, Variants và platform_mapping tại
@models/components.model.yaml (block button).
Thực hiện trọn vẹn từ Step 1 đến Step 7: TDD -> Code -> Preview Canvas ->
Visual Snapshot -> Dispatch Dual Sub-Agents.
Cập nhật nhịp tim định kỳ vào ../../.agy/heartbeat.
Sau khi hoàn tất và cả 2 Sub-agent cùng PASS, xuất báo cáo tổng kết ra file
../../.agy/last-run.json." --yes > ../../.agy/execution.log 2>&1 & echo $! >
../../.agy/worker.pid

cd ../..

None‎

### Step 3: Asynchronous Observation & Deadlock Prevention

Trong lúc `agy` thực thi:

### 1. **Heartbeat & PID Monitoring (Master Muse)**
* Muse kiểm tra file `.agy/heartbeat` và process PID.
* Nếu nhịp tim cập nhật đều -> Cập nhật `state = "EXECUTING"` hoặc `state =
## "AUDITING"`.
* Nếu quá 3 phút không có nhịp tim mới hoặc timeout 10 phút -> chạy `kill -9
$(cat .agy/worker.pid)`, xóa worktree và kích hoạt khắc phục.

### 2. **Worker Local Healing (Tier 1)**
* `agy` bên trong Worktree tự động xử lý Tier 1 Local Healing (tối đa 3 vòng
lặp đối kháng với Dual Sub-Agents).

### Step 4: Output Parsing, Failure Taxonomy & State Checkpoint

Khi tiến trình `agy` kết thúc, Muse đọc `.agy/last-run.json`:

* **Trường hợp 1 (`status == "PASS"`)**
1. Muse chuyển sang `.worktrees/button`, tạo commit chuẩn và merge nhánh
`worker/button` vào `feature/phase-2-components`.
2. Muse xóa worktree tạm thời: `git worktree remove --force
.worktrees/button`.
3. Muse cập nhật `.agy/state.json`: `state = "CHECKPOINTED"`, đưa component
vào `completed_components`.
4. Muse trích xuất ảnh `visual_snapshot` và dispatch component tiếp theo.

* **Trường hợp 2 (`status == "REJECT"` hoặc Exit Code khác 0)**
1. Muse đọc `error_code` (Failure Taxonomy):
- `ERR_SPEC_DRIFT`: Chèn chỉ thị "Khóa cứng props/variants bám sát
@models/".
- `ERR_TOKEN_LEAK`: Chèn chỉ thị "Thay thế toàn bộ mã hex/pixel thô bằng
token alias".
- `ERR_WCAG_CONTRAST`: Chèn chỉ thị "Tăng độ tương phản màu lên tối thiểu
4. 5:1".
2. Nếu `attempt_count < 3`: Muse rollback worktree và chạy lại lệnh với
prompt gia cố (`state = "RETRYING"`).

3. Nếu `attempt_count >= 3`: Kích hoạt **Human Circuit Breaker**, giữ nguyên
worktree để kiểm tra và gửi báo cáo xin chỉ đạo (`state =
## "HUMAN_INTERVENTION"`).

### Step 5: Final Delivery & Mobile Reporting (Muse -> User)

Khi toàn bộ linh kiện của Phiên hoàn tất:

1. Muse dọn dẹp toàn bộ worktrees, đẩy nhánh feature lên GitHub remote và tạo
Pull Request:
```bash
git push origin feature/phase-2-components

2. Muse gửi thông báo hoàn tất duy nhất về điện thoại cho người dùng kèm các ảnh chụp
màn hình thực tế:

None‎
[MUSE REPORT - PHIÊN 2 HOÀN TẤT (v2.0 GITHUB HARDENED)]
Đã nghiệm thu tự động thành công toàn bộ 5 components trong Git Worktrees cô
lập: Button, InputField, Card, Modal, Toggle.
- 100% Unit Tests & Dual Sub-Agent Review: CONSENSUS PASS
- Zero Workspace Pollution: All worktrees cleaned and merged
- Git PR đã tạo: feature/phase-2-components -> main
(Đính kèm 5 ảnh snapshot ma trận trạng thái bên dưới để bạn duyệt trực quan)

## 4. BẢNG TIÊU CHÍ NGHIỆM THU KIẾN TRÚC (EXIT CRITERIA)

Tiêu chí                               Trạng thái                        Cơ chế kiểm chứng

Phân định trách nhiệm rõ ràng          PASS                              Master Muse giữ vai trò chiến
lược; Worker agy độc quyền
code/test

Headless Execution Protocol            PASS                              100% lệnh gọi sử dụng --yes
non-interactive chế độ nền

Tiêu chí                        Trạng thái   Cơ chế kiểm chứng

Isolated Git Worktrees          PASS         Mỗi component chạy trong
.worktrees/[component],
zero workspace pollution

State Machine Enum &            PASS         Trạng thái rõ ràng (IDLE,
Checkpointing                                EXECUTING, AUDITING,
CHECKPOINTED), tự resume

Structured Failure Taxonomy     PASS         Phân loại lỗi chuẩn
## (ERR_SPEC_DRIFT,
## ERR_TOKEN_LEAK,
## ERR_WCAG_CONTRAST)

Async Observer & Heartbeat      PASS         Giám sát nhịp tim định kỳ qua file
Tail                                         .agy/heartbeat, phát hiện và
ngắt deadlock

Quy trình Self-Healing 2 tầng   PASS         Tier 1 (Worker local, 3 loops) &
Tier 2 (Master Escalation) hoạt
động đúng

Human Circuit Breaker           PASS         Tự động kích hoạt khi vượt quá 3
lần lặp local + 1 lần escalation

Giao ước State & Contract       PASS         File .agy/last-run.json được
cập nhật chuẩn xác sau từng
task

Xác thực Google Auth SSO        PASS         Tái sử dụng phiên đăng nhập
Google Auth SSO có sẵn, không
rò rỉ secret

Khởi động nguội tự hành         PASS         Muse AI tự kiểm tra môi trường,
(Cold-Start)                                 clone repo và tự động kích hoạt
script setup

Báo cáo trực quan Mobile        PASS         Đính kèm đầy đủ ảnh snapshot
PNG nghiệm thu trực tiếp trong
giao diện chat


## v3.0 ADDENDUM — MANDATORY SECURITY AND QUALITY GATES

This addendum is normative and supersedes any conflicting v2.0 statement that permits
merge, PR readiness, or completion based only on the two existing visual/code auditors.

### Canonical gate states
Use only: `NOT_RUN`, `PASS`, `FAIL`, `BLOCKED`, `ARBITRATION`, `FLAKY`.
A missing, malformed, stale, or absent required artifact is `BLOCKED`, never `PASS`.
`ARBITRATION` is a pending human decision and is never merge-eligible.
`FLAKY` is not a pass; it blocks release until rerun evidence establishes a stable
result or an explicitly authorized, documented exception is granted. No AI agent is
a human approver.

### Required security dispatch and aggregation
For every Phase 2 component task and every Phase 3 screen task, Worker MUST dispatch
a separate Security Reviewer with fresh context after implementation and before
final arbitration. The reviewer receives the task diff, base/head commit identifiers,
changed-path list, applicable contracts, and SECURITY_REVIEW.md. It is strictly
read-only: no code, test, configuration, or baseline mutation; no write permissions.
It must emit `.agy/security-review.json` and a human-readable report. The JSON must
include schema_version, task_id, base_sha, head_sha, changed_paths, reviewer_id,
reviewed_at, status, findings[], checks[], and report_path. A result is valid only
when it identifies the exact audited head SHA and all mandatory checks are present.

Master MUST independently validate the artifact and SHA freshness. Missing dispatch,
missing artifact, invalid schema, mismatched SHA, skipped checks, reviewer write
activity, unresolved security findings, or a failed security check => BLOCKED/FAIL.
The security veto is absolute for ordinary orchestration: Master, Worker, visual
auditors, and code auditors cannot override it. Only a named human owner may resolve
a finding through a documented remediation and a fresh security review; a human
exception may not waive a confirmed critical vulnerability or secret exposure.
Security PASS is required before merge, PR-ready status, release, and final PASS.

### Phase 2 / Phase 3 completion contract
A task is merge-eligible only when every required platform-specific regression check
is PASS, both phase-specific auditors are PASS, the independent Security Reviewer
is PASS, component freeze/drift checks are PASS, and no finding is unresolved.
Any remediation invalidates all prior test, visual, review, and security evidence
for the changed task. Rerun the complete phase regression and all affected reviewers
against the new head SHA. Phase 3 uses the full regression matrix defined in
docs/specs/phase-3.md; E2E-only reruns are insufficient.

### Human risk approval
Defect severity (P0/P1/P2) is not change risk. Master must separately classify change
risk using changed paths, data sensitivity, privilege boundary, blast radius, and
release impact. LOW may complete autonomously only after every gate passes.
MEDIUM requires at least one human approval. HIGH requires explicit owner approval
and the stricter approval policy defined by the project owner. AI agents never count
as human approvers. Recompute risk whenever scope expands.

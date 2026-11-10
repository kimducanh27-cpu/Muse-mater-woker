# THE SEED — Human-Gated Product Discovery

**Cấu hình đã chốt:** AI = **Sparring** · Research = **Deep** · Antigravity = **3 tabs**.

The Seed chuyển một ý tưởng thô thành một **product seed có căn cứ và được con người duyệt**, đủ rõ để bàn giao sang giai đoạn App Flow. The Seed không tự viết PRD, không tạo App Flow/UX/UI và không triển khai ứng dụng.

## Định hướng kiến trúc đã sửa

Nguyên tắc mới là **upstream-first, orchestration-second**:

1. **Không viết lại Skill upstream chỉ để đổi tên.** Skill Product Brainstorming của Anthropic được lưu nguyên văn tại `.agents/skills/product-brainstorming/SKILL.md`, kèm license và thông tin nguồn.
2. **The Seed không phải bản fork trá hình.** `seed-explore` là lớp adapter/workflow riêng: gọi và áp dụng Skill upstream, sau đó thêm ranh giới Tab 01, artifact và Gate 1. Nội dung upstream không bị sửa.
3. **Chỉ tự viết phần thực sự đặc thù.** Deep Research, Independent Review, ba prompt khởi chạy, templates và các cổng duyệt là phần điều phối riêng của The Seed.
4. Skill Product Shaping của ferminrp được lưu ở `upstream/` như nguồn tham khảo nguyên bản, **không kích hoạt trong ba tab**. Nó là quy trình shaping end-to-end (có research, prototype và shaping doc), trong khi The Seed cố ý tách ba vai trò và kết thúc trước App Flow. Bật nó đồng thời sẽ làm mờ ranh giới các tab.

Chi tiết nguồn, commit/blob và trạng thái license: xem [UPSTREAMS.md](UPSTREAMS.md).

## Cấu trúc

```text
.agents/skills/
├── product-brainstorming/       # Upstream Anthropic — nguyên văn
├── seed-explore/                # Adapter Tab 01 — custom
├── seed-research/               # Deep Research — custom
└── seed-independent-review/     # Fresh-context review — custom

upstream/
└── ferminrp/product-shaping/    # Upstream source, reference-only
    ├── SKILL.md
    └── references/
        ├── prototype-guide.md
        └── shaping-doc-template.md

prompts/
├── 01-TAB-EXPLORE.md
├── 02-TAB-DEEP-RESEARCH.md
└── 03-TAB-INDEPENDENT-REVIEW.md

templates/
├── 01-SEED-CANDIDATE.md
├── 02-RESEARCH-DOSSIER.md
├── 03-DECISION-LOG.md
├── 04-SEED-REVIEW.md
└── 05-SEED-FINAL.md

product/seed/                    # Artifact được tạo cho từng ý tưởng
UPSTREAMS.md
LICENSES/
```

## Cài vào Antigravity

1. Clone repo này hoặc đưa các file trong repo vào **workspace root** của dự án Android.
2. Giữ nguyên thư mục `.agents/skills/` ở workspace root.
3. Mở Antigravity IDE → Agent side panel → **Customizations**, xác nhận bốn skill đang hoạt động được phát hiện.
4. Tạo ba conversation/tab riêng biệt, cùng trỏ vào một workspace.
5. Mỗi tab dùng đúng prompt tương ứng trong `prompts/`. Không dùng lại lịch sử chat của tab trước; artifact trong workspace là nguồn sự thật.

Antigravity IDE hỗ trợ workspace skill ở `<workspace-root>/.agents/skills/<skill-folder>/`; có thể kiểm tra trong Customizations. Tài liệu: https://antigravity.google/docs/skills

## Quy trình 3 tab

### Tab 01 — Explore / Sparring

Dùng `product-brainstorming` (upstream nguyên văn) cùng `seed-explore` (adapter).

- Làm rõ người dùng, bối cảnh, vấn đề, workaround và outcome.
- Sparring với giả định; chỉ divergent brainstorm khi problem framing đủ rõ.
- Không web research ở tab này.
- Tạo `product/seed/01_SEED_CANDIDATE.md` và khởi tạo `03_DECISION_LOG.md`.
- Dừng ở **Gate 1**. Chỉ ghi nhận duyệt khi bạn nói rõ `APPROVE GATE 1`.

### Tab 02 — Deep Research

Dùng `seed-research` trong một conversation mới.

- Chỉ chạy sau Gate 1 đã được duyệt.
- Kiểm tra vấn đề/người dùng, sản phẩm thay thế, repo open-source, constraint Android và các giả định rủi ro.
- Ưu tiên nguồn sơ cấp; mở nguồn quan trọng; ghi URL, ngày kiểm tra, bằng chứng ủng hộ/phản bác và giới hạn.
- Tạo `product/seed/02_RESEARCH_DOSSIER.md`.
- Dừng ở **Gate 2**. Chờ `APPROVE GATE 2`, `MORE RESEARCH: ...` hoặc `RETURN TO EXPLORE: ...`.

### Tab 03 — Independent Review

Dùng `seed-independent-review` trong conversation mới, không dựa vào lời kể từ hai tab trước.

- Chỉ chạy khi Gate 1 và Gate 2 đều có approval tường minh.
- Review artifact và evidence traceability; không tự sửa candidate/research.
- Tạo `product/seed/04_SEED_REVIEW.md`.
- Review tối đa ba vòng; không lặp lại finding đã đóng nếu không có bằng chứng mới.
- Dừng và chờ quyết định của bạn. Chỉ lệnh chính xác `FREEZE SEED` mới cho phép tạo `product/seed/SEED.md`.

## Human gates — không tự động handoff

| Gate | Người dùng duyệt | Nếu chưa duyệt |
|---|---|---|
| Gate 1 | Problem, primary user/context, hướng cần nghiên cứu | Tab 01 tiếp tục chỉnh hoặc dừng |
| Gate 2 | Bằng chứng và việc có tiếp tục hay không | Tab 02 bổ sung nghiên cứu hoặc quay lại Tab 01 |
| Gate 3 / Freeze | Review và rủi ro còn lại | Không tạo SEED.md |

Không có master orchestrator, subagent, webhook, auto-run hoặc auto-handoff. Một agent nói “đã xong” không phải approval. Im lặng hay phản hồi tích cực cũng không phải approval.

## Quy tắc chất lượng

- Sparring mạnh vào luận điểm, không công kích người dùng và không bất đồng để diễn.
- Hỏi một câu chính mỗi lượt; không đưa bảng câu hỏi dài để người dùng điền.
- Phân biệt USER-CONFIRMED / USER-REPORTED / EVIDENCE / INFERENCE / HYPOTHESIS / UNKNOWN.
- Stars, downloads và marketing copy không chứng minh nhu cầu hay chất lượng.
- Repo được nhắc tới phải kiểm tra license và trạng thái bảo trì; không có license thì không hàm ý được phép tái sử dụng.
- Không bịa số liệu. Thiếu dữ liệu ghi `NOT FOUND` hoặc `NOT VERIFIED`.
- The Seed không tạo PRD, feature spec, App Flow, UX, UI, design system, database, architecture hoặc code.
- `SEED.md` chỉ là bàn giao sang App Flow; không tự khởi động giai đoạn đó.

## Artifact của một dự án

Các file trong `product/seed/` là đầu ra theo từng ý tưởng, không phải dữ liệu mẫu có sẵn. Xem [product/seed/README.md](product/seed/README.md).

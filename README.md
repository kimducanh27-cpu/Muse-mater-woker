# THE SEED — Human-Gated Product Discovery

**Cấu hình The Seed đã chốt:** AI = **Sparring** · Research = **Deep** · Antigravity = **3 tabs**.

The Seed là quy trình đầu tiên: biến ý tưởng thô thành một problem/idea seed có cấu trúc và được con người duyệt. Nó không thay thế Product Discovery và không tạo PRD, App Flow, UX/UI hay code.

## Kiến trúc

Nguyên tắc chung: **upstream-first, orchestration-second**.

- Skill upstream phù hợp được giữ nguyên văn và có nguồn/license.
- Logic riêng của workspace nằm trong adapter và prompt riêng.
- Không đổi tên một bản viết lại thành Skill upstream.
- Không tự động chuyển quy trình; mỗi giai đoạn có human gate.

## Quy trình 01 — The Seed

### Cấu trúc

```text
.agents/skills/
├── product-brainstorming/       # Anthropic upstream — unchanged
├── seed-explore/                # Tab 01 adapter
├── seed-research/               # The Seed's deep-research gate
├── seed-independent-review/     # Fresh-context review
└── product-discovery/           # Process 02 — separate kit

upstream/ferminrp/product-shaping/ # Reference-only upstream
prompts/                           # Three The Seed tab prompts
templates/                         # The Seed artifact templates
product/seed/                      # Per-idea The Seed artifacts
product-discovery-kit/             # Process 02 kit documentation
```

Chi tiết Skill upstream và nguồn: [UPSTREAMS.md](UPSTREAMS.md).

### Quy trình 3 tab

**Tab 01 — Explore / Sparring**
- Làm rõ người dùng, bối cảnh, vấn đề, workaround và outcome.
- Chỉ divergent brainstorm sau khi framing đủ rõ.
- Không external research.
- Tạo `product/seed/01_SEED_CANDIDATE.md`.
- Dừng tại Gate 1; chỉ chấp nhận lệnh `APPROVE GATE 1`.

**Tab 02 — Deep Research**
- Chỉ chạy sau Gate 1.
- Thu thập bằng chứng về vấn đề, lựa chọn thay thế, repo/open source, Android constraints và giả định rủi ro.
- Ưu tiên nguồn gốc, evidence traceability, phản chứng và giới hạn.
- Tạo `product/seed/02_RESEARCH_DOSSIER.md`.
- Dừng tại Gate 2.

**Tab 03 — Independent Review**
- Fresh context, chỉ đọc artifact và evidence.
- Review tối đa ba vòng.
- Không tự sửa quyết định của người dùng.
- Chỉ tạo `product/seed/SEED.md` khi người dùng ra lệnh `FREEZE SEED`.

### Ranh giới bàn giao

`SEED.md` là đầu vào cho **Quy trình 02 — Product Discovery**, không phải chỉ thị tự động tạo App Flow. Xem [Product Discovery Kit](product-discovery-kit/README.md).

---

## Quy trình 02 — Product Discovery

Kit độc lập tại [.agents/skills/product-discovery/SKILL.md](.agents/skills/product-discovery/SKILL.md).

Product Discovery lấy Seed làm đầu vào, sau đó khám phá cơ hội, thu thập bằng chứng từ người dùng, phân tích giả định và thiết kế thí nghiệm kiểm chứng. Bộ này có ba tab riêng: Opportunity Discovery, Customer Evidence, Solution & Experiments.

Đầu ra là Discovery Outcome có mức độ bằng chứng rõ ràng; **không phải PRD, App Flow, UX/UI hay code**. Xem [README của kit](product-discovery-kit/README.md).

## Cài vào Antigravity

1. Clone repo hoặc đưa nội dung vào workspace root của dự án.
2. Giữ thư mục `.agents/skills/` ở workspace root.
3. Mở Agent side panel → **Customizations** để kiểm tra Skills.
4. Mỗi process dùng đúng prompt và artifact trong workspace; không dựa vào chat history của tab khác.

Antigravity IDE hỗ trợ workspace skills tại `.agents/skills/<skill-folder>/`. Tài liệu: https://antigravity.google/docs/skills

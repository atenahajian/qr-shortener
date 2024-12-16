export interface UrlResponse {
    id: number;
    short_code: string;
    original_url: string;
    qr_code_path: string | null;
    created_at: string;
    expires_at: string | null;
    click_count: number;
  }
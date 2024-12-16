'use client';

import React from 'react';
import QRCode from 'qrcode.react';
import { UrlResponse } from '@/lib/types';

interface QRDisplayProps {
  urlData: UrlResponse;
}

export function QRDisplay({ urlData }: QRDisplayProps) {
  const shortUrl = `${window.location.origin}/${urlData.short_code}`;

  return (
    <div className="space-y-6 rounded-lg bg-white p-6 shadow">
      <div>
        <h3 className="text-lg font-medium text-gray-900">Your Shortened URL</h3>
        <div className="mt-2">
          <a
            href={shortUrl}
            target="_blank"
            rel="noopener noreferrer"
            className="text-indigo-600 hover:text-indigo-500"
          >
            {shortUrl}
          </a>
        </div>
      </div>

      <div>
        <h3 className="text-lg font-medium text-gray-900">QR Code</h3>
        <div className="mt-4 flex justify-center">
          <QRCode value={shortUrl} size={200} />
        </div>
      </div>

      <div className="mt-4">
        <p className="text-sm text-gray-500">
          Total Clicks: {urlData.click_count}
        </p>
      </div>
    </div>
  );
}